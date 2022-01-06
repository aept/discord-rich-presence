# <p align="center">Discord Rich Presence</p>

This a simple console app which can customize your Discord Presence easily, with only one config file!

# Setup

 1. Go to <a href="https://discord.com/developers/applications" target="_blank">Discord Developers</a>
 2. Then click on **New Application**

      ![Discord Developers - Applications](https://i.imgur.com/vhosxCU.png)
  
 3. Give it a name


      ![App Name](https://i.imgur.com/dQFg9JY.png)
  
 4. Click on **Create** button, then go to **Rich Presence** 

      ![Rich Presence Button](https://i.imgur.com/6mdhnnh.png)
  
 5. Upload your images and give them a name

      ![Images upload](https://i.imgur.com/KzMYoTy.png)
  
 6. Once you do the last steps go to **General Information** and copy your **Application ID**

      ![Application ID](https://i.imgur.com/HQbqWFh.png)
  
 7. It's done! 🎉, now paste the **Application ID** into the config file and run the app!

      ![Result](https://i.imgur.com/6Xhzsfm.png)

# Presence Config

The app will crash if you delete config file.
##### config.json
```json
{
	"applicationId": "Your Application ID.",
	"presenceId": 0,
	"timestamps": true,
	"presences": [
		{
			"state": "State here",
			"details": "Details here",
			"assets": {
				"small_text": "Small text here",
				"small_image": "Small image here",
				"large_text": "Large text here",
				"large_image": "Large image here"
			},
			"buttons": [
				{
					"label": "Button name here",
					"url": "Url here"
				}
			]
		}
	]
}
```
