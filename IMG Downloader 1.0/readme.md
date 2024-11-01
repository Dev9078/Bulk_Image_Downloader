you need a *IMG link Fetcher.py* for that for faster work.
if we want to fetch img sources list from any kind of website we needed to use IMG link fetching.

*you need to understand the code first to use later*
*This instruction is for only 1.0 versions*

Info About IMG Downloader 1.0:
    it is a basic bulk image downloader based on python
1. just run the ragalahari Image_Donwloader.py in needed folder

2. follow the steps to include specific gallery into your folder
    -> go to ragalahari.com or idlebrain.com
    -> click on actor/actress gallery you want to download
    -> click on first image of perticular gallery
    -> at last copy the URL of the first image
    -> it should as per given:

        old type: https://img.ragalahari.com/gallery/kajalpink/kajalpink1.jpg
        new type: https://m.ragalahari.com/actress/79923/heroine-ritika-singh-photos/image1.aspx
    
    -> if the url is old type than there is no problem but,
    -> if the url is new type
    -> 1st download the .aspx extension after downloading it open that file into an source code editor which has index nmber system
    -> after opening .aspx file on line 344 or 369 of html you can see the
        
        img src= "https://starzone.ragalahari.com/nov2016/posters/ritika-singh-shivalinga/ritika-singh-shivalinga1.jpg"
            
            -> just copy source url and paste it like below

3. Enter Details as pe below
    Enter URL: https://starzone.ragalahari.com/nov2016/posters/ritika-singh-shivalinga/ritika-singh-shivalinga
    <!-- do not enter the last image number and extension e.g.: 1.jpg -->
    Start Index Number: 1
        <!-- it will always start from 1 or whenever you want to start from -->
    End Index Number: 
        <!-- Enter as needed 10/20 or you can see the last image of the gallery for the last index number -->
    Enter File Extension: .jpg
    Enter Folder Name: (Enter Path or Enter Name)
        <!-- The new folder will created automatically in downloder.py parent folder -->