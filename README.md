# Facebook Operations


Note: Selenium Has Been Used For Making The Bot
===============================================================================================================================================================================

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Key Features And Point:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The Given Project Takes The Facebook Username And Password And Does The Following Operaions:

1. Login
   (Demo: https://drive.google.com/file/d/1NwGL2Ih7Pu5gayN5HsU_6RhZ-02lVCnu/view?usp=sharing)

2. Update The User's Status
   (Demo: https://drive.google.com/file/d/1QiWtb9PWCNC0O1_ezJ4MeBoT4vurWtFz/view?usp=sharing)

3. Add A Freind Who Lives In The Same Location (City) As User
   (Demo: https://drive.google.com/file/d/1cysI1Xv9T9jBxKgfXR0dOFn-5f6I6l6C/view?usp=sharing)

4. Comeents On The Latest First Post Of A Random Friend (The Comment Is Passed Through A Funciton Call In The Code)
   (Demo: https://drive.google.com/file/d/1iWZIyJ_NbeI097UKduK7TFMGkWjwKWMZ/view?usp=sharing)

-> The Project Is Fully Dynamic. It Does Not Involve Aany Hardcoded Url Links Except For Facebook's Home Page. 

-> The Html Elements Like Text Area, Buttons, Etc Arre Assumed To Begeneric For Different Users, Meaning That The Html Element Path For A Particular Text Area Like "What's On Your Mind" Is The Same For Different Users As Ouline Of The Html Pafe Remins Constant Thus Their Hardcoded Element References Does Not Effeect The Dynamic Nature Of The Application.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Assumptions Made:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A) When The Facebook Page Of The User's Current City Is Opened For Sending Friend Request To A Person In The Same Location, It Is Assumed That The First Post On The Page Is From A Person And Not Any Public Organisation. Only Then Could The "Add Friend" Button Be Access By The Code. 

B) With Reference To The Previous Point, It Is Also Assumed That The Perosn With The Latest Post On The City Page Is Related To The  City Itself As There Is Less Chace That He/she Would Post Abouut The City When He Is Not Form There.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Procedures Carried Out For Various Tasks:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1> For Adding Friend From The Current City, The Bot First Goes To "About" Section Of The Current User, Browses Through The Cities He Has Lived And As The Current City Is Usually Listed At Top. It Click The City Url And Is Directed To The Facebook Page Of The City. Then According To Assumptions (A) And (B), It Adds The Very First Person On The Page As The Friend

2> For Poting On The Timeline Of A Random Friend, The Bot Goes To The "Friends" Section Of The User And Picks The First Friend And Posts On Their Timeline. It Is To Be Noted That The Way Friends Are Shown On Facebook "Friends" Section Varies With Time. Thus The Randomness Is Maintained. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
User Guide:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1> The User Would Need To Clone The Repository And Enter His Credentials In The Files "Test" Folder (Ex : Lines 24 And 25 In "Login_test.py") 

2> Install The Dependencies As Mentioned In Requirements.txt

3> Download The Chrome Driver From https://chromedriver.chromium.org/downloads, Unzip The File And Paste The Execution File The "Python Folder"
 (Ex : C:\users\user\appdata\local\programs\python\python39)
 
3> Run The Test File From The IDE Interface Itself (Preferably PyCharm) And Not The Terminal

4> Enjoy!
