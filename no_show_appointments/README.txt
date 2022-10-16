# No show appointmets project

## by Mostafa Elnagar 

## Dataset

This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row.

## Questions to Explore:
first we will define waiting time as the number of days from registering for an appointment untill the appointment day.

- Is gender of the patient related to showing up in the appointment?
- Is receiving an SMS affect showing up in the appointment?
- Is having a scholarship somehow related to showing up?
- What is the proportion of patients who have been diagnosed with Diabetes, Alchoholism, Handicap or Hypertension - - and show up to those who have but didn't show up?
- What is the showing up rate associeted with each neighbourhood?
- What is the age distribution and is there a range where it is more likely to show up?
- Is there a relationship between the waiting time and the number of patients showing up?
 ## Findings
- approximately 20% of the patients didn't show up in there appointments
- the gender of the patient isn't related to showing up in the appointment since males have a showing up percentage 80.03% and females have a showing up percentage 79.69% so close to be the same.
- 32.11% of the patients recieved an SMS
- 72.43% of those who recieved an SMS showed up and 83.30% of those who didn't receive an SMS showed up
- People who didn't recieve an SMS have a showing up percentage higher by 10.87% than those who recieved
- 29.13% of people who showed up received an SMS and 43.84% of people who didn't show up received an SMS.
> so based on these facts we see that although the proportion of people who should up from those who didn't receive an SMS is higher we can't say that there is a correlation here.

- 76.26% of people who have a scholarship show up and 80.19% of people who have no scholarship show up.
- 11.55% of the people that didn't show up have a scholarship thats higher than those who did show up by 2.16% and this difference is relatively big.
- 82% of patients were having a special condition and show up and only 18% didn't show up.

## Limitations
- only a very small proportion of the data is diagnosed with special cases and that makes the results not reliable.
- the documentation of the dataset was ambigous regarding the appointment_day and scheduled_day columns so it might affect the conclusions.
- in the handicap column there was values greater than one so we casted it to 1s this might be incorrect and affect the conclusions.
