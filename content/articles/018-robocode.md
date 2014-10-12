Robocode
===================
**Title:** Robocode
**Date:** October 12th, 2014
**Tags:** Robocode, Tutorial
**Category:** Introduction
**Author:** René Birkeland


Robocode is a simple robot simulator, designed to give insight into how programming works. A simple robot can be written in just a few minutes - but perfecting a bot can take months. The robots will enter the battlefield and fight to the death.

-- PELICAN_END_SUMMARY --

----------


How to install
-------------

Robocode is written in Java, and can easily be installed simply by running the **.jar file**.

1. Go to [this link](http://sourceforge.net/projects/robocode/files/robocode/1.9.2.3/).
2. Choose **robocode-1.9.2.3-setup.jar** and save it somewhere you can easily find it, like your desktop.
3. Run the file, and follow the instruction. Install it somewhere you will remember (you will need to know later).
4. After completion, you will have a desktop icon, double click it to run Robocode.

----------


Get familiar
-------------------

To get a feeling how Robocode works, let's do a quick demonstration how the robots act.

Start by clicking **Battle** in the top menu, and choose **New**. Here you will see a list of sample robots. By looking at the names, you might be able to guess how to robots will act. Pick 3-5 different ones you like, by selecting one and clicking **Add**. You can also remove robots that are selected by pressing **Remove**.

When you've selected your desired contestants. Click **Start Battle** to begin.

The robots will start to fight. In the window you will have several buttons and sliders. In the left bottom corner you find your typical **Start/Stop/Pause** functionality among others. On the bottom of the screen you will have a slider to control the speed of the match.

A match consists of 10 rounds, and the robots gather points based on how well they do. The total score is calculated from:

 - How long it survives.
 - How much damage it deals to other robots (bullets or ramming).

> **Note:**

> The best robot is not necessarily the last one standing. Find the perfect balance between surviving, and dealing damage.

Spend some time testing the different sample robots, gather ideas on how you want your robot to work.

---------

Make your own robot
-------------

Now that you have seen how Robocode works, it's time to make your own!

1. Click on **Robot** -> **Source Editor** to open the editor.
2. To make a new robot simply click **File** -> **New** -> **Robot**.
3. Give your robot a good name. 
4. Use your team's name package name

You will now be presented with the editor. It has already some code in it to give you a start. Take a look through it, and make sure to read the comments, they have a lot of useful information.

Lets go through the most important methods.

###Methods

```java
public void run() {}
```

This is the main method. This is were the majority of your robots behavior is defined. It should have a while-loop that continues to run forever, for example by using **while(true)**, like in the example code.

> **Note:**
> A while-loop is a loop that will run as long as the statement between the brackets is true. If you put **true**, it will run forever. If you put **i < 2**, it will only run as long as the variable **i** is less than 2. 

What you write before the while-loop will only get executed once. Here you can have your initialization of your robot. You can change the color of the robot, set a starting position of the gun, or get information about the battlefield size and heading (this is more complicated).

Inside the while-loop you will write the algorithm that control your robot. Don't be intimated by the word algorithm, no prior knowledge is needed. By looking at the example code you can see some simple examples.

- **ahead(100);** will move the robot 100 pixels forward.
- **turnGunRight(360);** turns the gun 360 degrees, a full resolution.
- **back(100);**  will move the robot 100 pixels backwards.

> **Note:** 
> You choose the values, depending how much you want to move or turn. They are not set in stone.

You can put as many lines as you want in the loop, but remember the loop will be repeated infinitely. It does not need to be very long to be effective.

--------

```java
public void onScannedRobot(ScannedRobotEvent e) {}
```
This method will automatically get called if another robot is scanned. This method is called automatically by the game, as long as the robot is moving, turning its body, turning its gun, or turning its radar.

Here you write what you want to happen when a robot is scanned. Will you fire or retreat?

--------
```java
public void onHitByBullet(HitByBulletEvent e) {}
```
This get executed if you get hit. Is this the time to run away or fire all your guns?

--------
```java
public void onHitWall(HitWallEvent e) {}
```
This get executed if you hit a wall. You know at this point you can't go any further, maybe it's best to back up, or turn 90 degrees to get away.

----------

###Save & Compile

While designing it's smart to save your project to avoid loosing your work in case something goes wrong. When you have designed your robot, it's time to save and compile.

> **Note:**
> The compiler is what translates the code from a language we can understand (Latin alphabet), into a language the computer understands (binary, 0 and 1).

Simply press **Compiler** -> **Compile**, or press **ctrl+B**.

After its compiled it's ready to see what you have made. Go back to the **Robocode window**, and start a new match like we did before, **Battle** -> **New**.

You will now see that your robot is in the list of robots. Add it, and maybe a few opponents to see how it works.

After testing it you might figure out that it does not work like you first intended, or you have come up with new improvements. In that case, go back to the editor and change your code again until you're happy wit the result. 

--------

Where can I find more methods and commands?
--------------------

Robocode has a bunch of built in methods and commands you can use to control your robot. So far we have only touched a few very basic ones. If you want to read more on how these method work or need to look up how to do certain things, take a look at these sites:

- [Robot Methods](http://robocode.sourceforge.net/docs/robocode/)
- [Robocode Wiki](http://robowiki.net/wiki/Robocode)

-----------------

Fight in the tournament (Robocode event)
----------------

When the time is up, you will have to deliver your robot. Remember it needs to be compiled!

1. To find it, locate the folder **"Robocode"** where you installed robocode.
2. Navigate to **Robots** and find the folder **"your team's name"**.
3. Make a copy of it and put it on your desktop.
4. Make sure it only contains the robot you want to submit, only 1 robot per team.
5. It **must** contain **yourRobot.java** and **yourRobot.class**.
5. We will pass around USB sticks, put the folder onto it.

Good luck!
