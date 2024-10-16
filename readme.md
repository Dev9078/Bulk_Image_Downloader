1. you need to understand the code first to use later

2. just run the ragalahari Image_Donwloader.py in needed folder

3. follow the steps to include specific gallery into your folder
    -> go to ragalahari.com or idlebrain.com
    -> click on actor/actress gallery you want to download
    -> click on first image of perticular gallery
    -> at last copy the URL of the first image
    -> it should as per given:

        old type: https://img.ragalahari.com/gallery/kajalpink/kajalpink1.jpg
        new type: https://m.ragalahari.com/actress/79923/heroine-ritika-singh-photos/image1.aspx

    -> if url is same as new one you need to go at chrome dev tools and on line 344 of html you can see the
        
        img src= "https://starzone.ragalahari.com/nov2016/posters/ritika-singh-shivalinga/ritika-singh-shivalinga1.jpg"
            
            -> just copy source url and paste it like below

4. Enter Details as pe below
    Enter URL: https://m.ragalahari.com/actress/79923/heroine-ritika-singh-photos/image

    Start Index Number: 1
        <!-- it will always start from 1 or whenever you want to start from -->
    End Index Number: 
        <!-- Enter as needed 10/20 or you can see the last image of the gallery for the last index number -->
    Enter File Extension: .jpg
    Enter Folder Name: (Enter Path or Enter Name)
        <!-- The new folder will created automatically in downloder.py parent folder -->

5. now it is almost ready if any problem occur contact me:
