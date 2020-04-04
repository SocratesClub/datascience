* Propensity Score Matching in Stata
* Copyright 2013 by Ani Katchova

clear all
set more off

* Download and install Stata ado files for pscore 
* net install st0026_2 

use C:\Econometrics\Data\matching_earnings

* Define treatment, outcome, and independent variables
global treatment TREAT
global ylist RE78
global xlist AGE EDUC MARR 
global breps 5

* For difference-in-differences, outcome is the differences in outcomes after and before
* global ylist REDIFF 

describe $treatment $ylist $xlist
summarize $treatment $ylist $xlist

bysort $treatment: summarize $ylist $xlist

* Regression with a dummy variable for treatment (t-test)
reg $ylist $treatment 

* Regression with a dummy variable for treatment controlling for x
reg $ylist $treatment $xlist

* Propensity score matching with common support
pscore $treatment $xlist, pscore(myscore) blockid(myblock) comsup

* Matching methods 

* Nearest neighbor matching 
attnd $ylist $treatment $xlist, pscore(myscore) comsup boot reps($breps) dots 

* Radius matching 
attr $ylist $treatment $xlist, pscore(myscore) comsup boot reps($breps) dots radius(0.1)

* Kernel Matching
attk $ylist $treatment $xlist, pscore(myscore) comsup boot reps($breps) dots

* Stratification Matching
atts $ylist $treatment $xlist, pscore(myscore) blockid(myblock) comsup boot reps($breps) dots

