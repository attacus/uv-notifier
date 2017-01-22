# UV Notifier
## Sends you an SMS when the UV levels dip below a safe point, or when they become too dangerous

### How to use this app
- sign up for a free [Twilio](https://www.twilio.com) account
- add your Twilio credentials as environment variables on your server (or wherever you're running this thing)
- run the app
- enjoy not getting sunburnt in Australia

## How to configure this app
The `city` variable in the Python script can be used to pull the UV index for the following Australian cities (must be properly capitalised, as below):
- Adelaide
- Alice Springs
- Brisbane
- Canberra
- Darwin
- Kingston
- Melbourne
- Newcastle
- Perth
- Sydney
- Townsville

You can set your own acceptable and dangerous UV levels using the `acceptable_uv` and `dangerous_uv` variables in the Python script. These must be in decimal format (e.g. 5.0) for the app to work properly.

To decide which UV levels are right for you, please check out the UV index information provided below.

### Please note:
This app pulls data from the [ARPANSA website](http://www.arpansa.gov.au/). These are official, up-to-date UV readings from the Australian Radiation Protection and Nuclear Safety Agency.

### UV Index info
For more information about ultraviolet radiation, [check the Wikipedia article](https://en.wikipedia.org/wiki/Ultraviolet_index).

| UV Index | Exposure Category |
| --- | --- |
| 2 or less |	Low |
| 3 to 5 | Moderate |
| 6 to 7 | High |
| 8 to 10 | Very High |
| 11+ | Extreme |

### Credits
This code took many pointers from https://github.com/JamesDaniel/DE-Novel-Website-Screen-Scraper

Data taken from [ARPANSA](http://www.arpansa.gov.au/).

### Disclaimer
I am not a doctor, and this app is not intended to be, nor should it be used as a replacement for medical advice from a qualified professional.
This app and associated code is in no way affiliated with ARPANSA, the Cancer Council of Australia, or any other organisation.
For more information about the relationship between UV and skin cancer, see the [Cancer Council of Australia website](http://www.cancer.org.au/preventing-cancer/sun-protection/) and/or consult your doctor.
