https://www.reddit.com/r/Runalyze/comments/16uddjf/comment/k2km5xn/?utm_source=share&utm_medium=web2x&context=3

laufhannes
·
13 days ago
Yes, Runalyze uses TRIMP^exp with the factors stated on the fellrnr wiki. For the moving average, by default, Runalyze uses the TSB model with the formula stated at https://fellrnr.com/wiki/Modeling_Human_Performance#The_TSB_Formulas

https://fellrnr.com/wiki/TRIMP

5 TRIMPexp Exponential Heart Rate Scaling
A more sophisticated approach uses Heart Rate Reserve and an exponential scaling factor to account for the fact that higher intensity training as a disproportionately high training impact[2][3][4]. The formula for calculating TRIMPexp is

TRIMPexp = sum(D x HRr x 0.64ey)
Where

D is the duration in minutes at a particular Heart Rate
HRr is the Heart Rate as a fraction of Heart Rate Reserve
y is the HRr multiplied by 1.92 for men and 1.67 for women.
These constants were developed based on the experimentally observed relationship between heart rate and lactate level. For men this will give a TRIMP value of 0 to 4.37 per minute and for women 0 to 3.4.

https://fellrnr.com/wiki/Modeling_Human_Performance#The_TSB_Formulas

2.4.1 The TSB Formulas
The basic formula for calculating ATL/CTL uses an Exponential moving average that is calculated like this:

ATLtoday = TRIMP _ λa + ((1 – λa) _ ATLyesterday
CTLtoday = TRIMP _ λf + ((1 – λf) _ CTLyesterday
