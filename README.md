# UV Notifier
## Sends you SMS updates about the UV in your Australian city

### How to use this app
- sign up for a [Twilio](https://www.twilio.com) account. This app will work on the Twilio free tier, but you'll have to put your Twilio number into the "from" field instead of a custom name.
- add your Twilio credentials as environment variables on your server (or wherever you're running this thing)
- run the app on the cron job or trigger of your choice. It is designed to be triggered twice - once in the morning 🌅, and once in the afternoon ☀️.
- enjoy not getting sunburnt in Australia!

## How to configure this app
To run the app manually, you must run `invoke notifier $YOUR_CITY` from the app directory, where `$YOUR_CITY` is one of the following Australian cities (or Antarctic stations) (must be properly capitalised, as below):

- Adelaide
- Alice Springs
- Brisbane
- Canberra
- Casey
- Darwin
- Davis
- Kingston
- Macquarie Island
- Mawson
- Melbourne
- Newcastle
- Perth
- Sydney
- Townsville

The acceptable UV range is set from `3.0`-`3.5` by default.
If you decide to alter this, please note the UV level must be in decimal format (e.g. `5.0` or `2.7`) for the script to work properly.

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
Data taken from [ARPANSA](http://www.arpansa.gov.au/).

### Disclaimer
I am not a doctor, and this app is not intended to be, nor should it be used as a replacement for medical advice from a qualified professional.
This app and associated code is in no way affiliated with ARPANSA, the Cancer Council of Australia, or any other organisation.
For more information about the relationship between UV and skin cancer, see the [Cancer Council of Australia website](http://www.cancer.org.au/preventing-cancer/sun-protection/) and/or consult your doctor.
