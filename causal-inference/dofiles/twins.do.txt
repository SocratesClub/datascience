*** Metrics
*** Table 6.2
*** Metrics returns to schooling for Twinsburg Twins

clear

// set to directory where data (pubtwins.dta) is located
cd ""

use "pubtwins.dta", clear

replace age2 = age2/100

/* plain regression */

reg lwage educ age age2 female white, robust
outreg2 using "../Output/twins.xls", replace bdec(3) sdec(3) noaster word


/*  Twins differences */

reg dlwage deduc if first==1,noconstant robust
outreg2 using "../Output/twins.xls", append bdec(3) sdec(3) noaster word

/* IV */

ivregress 2sls lwage (educ=educt_t) age age2 female white, robust
outreg2 using "../Output/twins.xls", append bdec(3) sdec(3) noaster word

ivregress 2sls dlwage (deduc=deduct) if first==1,noconstant robust
outreg2 using "../Output/twins.xls", append bdec(3) sdec(3) noaster word
