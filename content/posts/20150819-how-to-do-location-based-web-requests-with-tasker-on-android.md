Title: How to do location-based web requests with Tasker on Android
Date: 2015-08-19 08:40:58
Slug: 20150819-how-to-do-location-based-web-requests-with-tasker-on-android
Location: Train
Authors: Michiel Scholten
Tags: rant, howto, mobile
Category: howto

If you don't know [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) go and check it out now. It's by far the greatest way to automate, well, about everything on your Android device and its surroundings.

However, one thing it is not, is really easy to start with. If you tap through the interface for the first (and second and third) time you will likely be wondering how to even start thinkering with the idea you have.

So, in the light of the [ns-notifications service](https://github.com/aquatix/ns-notifications) I recently completely rebuilt, I'm going to have a small step-by-step guide to set up a new Profile, which triggers a Task when arriving at a certain wifi network (say, your work office or your home) and then do an http request. This will show the basics of how Tasker works and how to set up your own scripts.

A Profile is really just a set of triggers (or just one generally) that are linked to a Task to perform when activated by the situation. There is also an exit state, so if the situation stops, another Task can be run (for example, enable wifi when your home network is detected, disable it again when the network goes out of reach).

To start, go to the Profiles tab and tap the `+` button in the bottom bar. You will be presented with a small list of trigger types. Because being in range of a certain network is *state* and not an *event* for example, now tap State and choose Net in the next overview. 'Wifi Near' is the option we are now looking for. This is a service of your device (provided for example by the background scanning Android can do for you) that tells your Android what wifi networks are in range.

Now you are in the properties window of the State. Tap the search button next to SSID (looking glass icon) and choose the relevant network. You can choose more options, but for our use case, this is enough. Now go Back.

A menu pops up with a list of Tasks already configured, with at the top 'New Task'. Choose this item and type a name. You've now created a new Task that will be triggered when coming in reach of the wifi network.

This empty window is the script window. Here you can add Actions. Do so by tapping the now familiar `+` button. You can add an Alert for testing. If you choose an Action by accident and don't want to save, choose Cancel (might be in the overflow menu on your phone). Otherwise, configure if there is anything to set and go Back.

To create our web request, choose a Net task called 'HTTP Get'. Fill in the server and port (if applicable), so for example: 'example.com:4242'. The `server.py` of `ns-notifications` listens on port 8086 by default, so you might want to use that one instead. Under Path you put the rest of the url you want to request, so for example 'disable/work' to trigger the disable alerts on the server, noting you arrived at work. You can leave the rest empty, but might want to put in a timeout of about 10 seconds or so to be save the Task will not hang when connectivity fails.

We are done :) You successfully made a web request on entering a certain wifi network. Or did we do so successfully? The 'HTTP Get' Action sets a variable when exiting successfully, which you can check. This variable is called `%HTTPD` (all variables in Tasker are prepended with a `%`).

So, add an Action: Task, If. Condition for the If is `%HTTPD` and choose 'Set' from the button next to the input field. This if statement checks whether the variable is set. You can now for example show an alert on your phone that everything went well, adding an Else with an alert that your request failed.

    NS alerts disable because of arriving at %atLocation

    Response: %HTTPR %HTTPD

The response variable '%HTTPR' shows the status code of the `server.py` response (generally `200`, but `-1` in case of network failure) and '%HTTPD' shows the response body ('Disabling notifications') or just the string '%HTTPD' itself in case of network failure.

%atLocation is a global variable I set myself based on my travels. More on that in a later post.


## Further reading

A more elaborate example for actually retrieving information through a web call [can be found on this http-get example on the Tasker wiki](http://tasker.wikidot.com/http-get). Also, I just found [this page](http://apcmag.com/ultimate-guide-to-tasker-app-part-3-using-data-from-the-web.htm/) which is a continuation of a tutorial you might want to play with.

There's also [the Tasker Google+ community](https://plus.google.com/communities/110787685049943933094) with people writing tutorials, scripts and answering questions.
