*** Metrics
*** Table 1.1
*** goal: make table of health outcomes and characteristics by insurance status ***

* by Georg Graetz, August 6, 2013
* modified lightly by Gabriel Kreindler, June 13, 2014
* modified lightly by Jon Petkun, January 2, 2015
* modified lightly by Ryan Hill, Jan 31, 2020

pause on
clear all
set more off
cap log close

// set to directory where NHIS2009_clean.dta is stored
cd "/NHIS/Data/"

cap log using NHIS2009_hicompare.log, text replace

use NHIS2009_clean, clear


* select non-missings
	keep if marradult==1 & perweight!=0 
		by serial: egen hi_hsb = mean(hi_hsb1)
			keep if hi_hsb!=. & hi!=.
		by serial: egen female = total(fml)
			keep if female==1
			drop female
	
* Josh's sample selection criteria	
	gen angrist = ( age>=26 & age<=59 & marradult==1 & adltempl>=1 )
		keep if angrist==1
	// drop single-person HHs
	by serial: gen n = _N
		keep if n>1


* Prepare matrix to store results
	matrix results = J(15,6,.)
	matrix rownames results = "Health index" "se" "Nonwhite" "se" "Age" "se" "Education" "se" "Family Size" "se" "Employed" "se" "Family income" "se" "Sample size"
	matrix colnames results = "Husbands: Some HI" "Husbands: No HI" "Husbands: Difference" "Wives: Some HI" "Wives: No HI" "Wives: Difference" 

	matrix list results,format(%8.4f)
	
	local col = 1
	local row1 = 1
	local row2 = 2
	

 * Health status by insurance coverage and sex
	forval fem = 0/1 {
	qui sum hlth if hi==1 & fml==`fem' [ aw=perweight ]
		mat results[`row1',`col'] = r(mean)
		mat results[`row2',`col'] = r(sd)
		local ++col
		
	qui sum hlth if hi==0 & fml==`fem' [ aw=perweight ]
		mat results[`row1',`col'] = r(mean)
		mat results[`row2',`col'] = r(sd)
		local ++col

	reg hlth hi if fml==`fem' [ aw=perweight ], robust
		mat results[`row1',`col'] = _b[hi]
		mat results[`row2',`col'] = _se[hi]
		local ++col
	}
		
		local row1 = `row1' + 2
		local row2 = `row2' + 2

* Other characteristics by insurance and sex		
	foreach var in nwhite age yedu famsize empl inc {
		
		local col = 1
		forval fem = 0/1 {
		
		* means and SDs
			qui sum `var' if hi==1 & fml==`fem' [ aw=perweight ]
				mat results[`row1',`col'] = r(mean)
				local ++col
			qui sum `var' if hi==0 & fml==`fem' [ aw=perweight ]
				mat results[`row1',`col'] = r(mean)
				local ++col
				
		* mean comparisons 
			reg `var' hi if fml==`fem' [ w=perweight ], robust
				mat results[`row1',`col'] = _b[hi]
				mat results[`row2',`col'] = _se[hi]
				local ++col
						
		}		
		local row1 = `row1' + 2
		local row2 = `row2' + 2
	}
		
	* Sample sizes
	tab hi if fml == 0 [aw=perweight], matcell(x)
	mat list x
	
	mat results[`row1',2] = x[1,1]
	mat results[`row1',1] = x[2,1]
	
	tab hi if fml == 1 [aw=perweight], matcell(y)
	mat list y
	
	mat results[`row1',5] = y[1,1]
	mat results[`row1',4] = y[2,1]

* List results
matrix list results, format(%8.2f)		
		
	
* Output results	
putexcel set MM_Table1_1, replace
putexcel A1 = matrix(results), names nformat(number_d2)
	
cap log close
