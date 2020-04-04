*cd "/Users/alvaro/Library/Application Support/Stata/ado/personal/psestimate"
cd "C:\ado\personal\psestimate"

discard

use nswre74, clear
foreach k in 74 75 78 {
	gen u`k' = (re`k'==0)
	lab var u`k' "Unemployed `k'"
	lab var re`k' "Earnings `k'"
}
lab var treat Treatment
lab var age Age
lab var ed Education
lab var black Black
lab var hisp Hispanic
lab var married Married
lab var nodeg "No degree"
lab var age2 "Age squared"
drop *78

********************************************************************************
* PSM algorithm
********************************************************************************

psestimate treat
