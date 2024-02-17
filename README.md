# Eddies Ironworks
## Contents
- Demo
- Criteria
- Technologies
- Testing
- Bugs
- Deployment
- Credits
- Acknoeledgements

## Demo
![Am I Responsive](https://github.com/grant-britchford/Eddies_Ironworks/assets/145594323/758242e6-f3f5-4fca-b5bd-fef442c87ac7)

The live link is: https://eddiesironworks-de86615814ee.herokuapp.com/

## Criteria

I have created a back end data system for an Ironworks company who fabricate and weld their own gates, railings and other accesories and then sell them from their own shop.

## Technologies

- Python was the program language specifically used to run this app.
- Node.js was used as part of the deployment package.
- Heruko was used to Dploy the app on line
- GitHub was used to run and debug the code.

## Testing

Testing was carried out as the Python code was put in to make sure that it all worked as it should.

## Bugs

All bugs found during the programming stages were dealt with and corrected as the program was run.

## Deployment

To deploy the app you must create an Heruko account on Heruko.com. Once this is done, then please follow these steps.

- Log in to your Heruko account and in your dashboard click on Ctreate new app.
- On the next page give you app a name and select europe under countries dropdown if you are outside of the US. Then click on create app.
- On the project page that loads up, select the settings tab from the top of the page.
- In the settings go to Config Vars and click on reveal Config Vars. In the key tab enter your key name e.g 'CREDS' then copy the contents of your creds file on GitHub and paste into the Value Tab. When this has been done click on Add.
- Underneath the Config Vars section you will find the Buildpack section. Click on this and from the menu that displays, select Python and add the buildpack and then select Node.js and add this to the build pack.
- Before leaving please make sure that Python is above Node.js in the list, if not then click and drag Python to the top.
- Return to the top of the page and go to the Deploy tab. On this page you will 3 Deployment methods. Select GitHub.
- When selected it will ask for your repository name in GitHub, enter this and select search. Once it has found your repository then press the Connect button.
- You will then find an Automatic Deploy method and a Manual Deploy method. please read the description of both of these to select how you want to deploy.
- In this instance Manual was opted and Deploy branch was pressed. You will then see the program logs as the app is built.
- Once the app is successfully built you will receive a 'App built successfully' message with a view button underneath. Click on this to go the runnable app and make sure all works as normal.

## Credits

- Code Institute and their walkthrough videos.

## Acknowledgements

- Code Institute for their tutition.
- My Mentor Oluwafemi Medale, as always.
  
