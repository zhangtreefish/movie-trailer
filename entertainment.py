import media

toy_story = media.Movie(
	"A River Runs Through It",
	"two brothers growing up in Montana",
	"https://en.wikipedia.org/wiki/A_River_Runs_Through_It_(film)#/media/File:A_river_runs_through_it_cover.jpg",
	"http://images.search.yahoo.com/images/view;_ylt=AwrTcX_kGylWILMAhM42nIlQ;_ylu=X3oDMTIyZGp1NTRkBHNlYwNzcgRzbGsDaW1nBG9pZAM5ZWU5OGEwMWMyZDhmODQ2NjkxMDg0YzkyNWE5NGM2MQRncG9zAzMEaXQDYmluZw--?.origin=&back=http%3A%2F%2Fimages.search.yahoo.com%2Fyhs%2Fsearch%3Fp%3Da%2Briver%2Bruns%2Bthrough%2Bit%2Btrailer%2Byoutube%26n%3D60%26ei%3DUTF-8%26y%3DSearch%26type%3Dirmsd103%26fr%3Dyhs-iry-fullyhosted_003%26fr2%3Dsb-top-images.search.yahoo.com%26hsimp%3Dyhs-fullyhosted_003%26hspart%3Diry%26tab%3Dorganic%26ri%3D3&w=480&h=360&imgurl=i.ytimg.com%2Fvi%2F0dAe_2y6_c8%2Fhqdefault.jpg&rurl=http%3A%2F%2Fyoutube.com%2Fwatch%3Fv%3D0dae_2y6_c8&size=21.0KB&name=%3Cb%3ERIVER%3C%2Fb%3E+%3Cb%3ERUNS%3C%2Fb%3E+%3Cb%3ETHROUGH%3C%2Fb%3E+%3Cb%3EIT+Trailer%3C%2Fb%3E+-+%3Cb%3EYouTube%3C%2Fb%3E&p=a+river+runs+through+it+trailer+youtube&oid=9ee98a01c2d8f846691084c925a94c61&fr2=sb-top-images.search.yahoo.com&fr=yhs-iry-fullyhosted_003&tt=%3Cb%3ERIVER%3C%2Fb%3E+%3Cb%3ERUNS%3C%2Fb%3E+%3Cb%3ETHROUGH%3C%2Fb%3E+%3Cb%3EIT+Trailer%3C%2Fb%3E+-+%3Cb%3EYouTube%3C%2Fb%3E&b=0&ni=96&no=3&ts=&tab=organic&sigr=116luaadt&sigb=17chk5edn&sigi=118mvgq2a&sigt=12arn6c2t&sign=12arn6c2t&.crumb=Rp15jr97RYy&fr=yhs-iry-fullyhosted_003&fr2=sb-top-images.search.yahoo.com&hsimp=yhs-fullyhosted_003&hspart=iry&type=irmsd103")
#print(toy_story.storyline)
up = media.Movie(
	"Up",
	"A lonely old man and an orphan scout go on a journey in a balllon-hoisted house",
	"https://en.wikipedia.org/wiki/Up_%282009_film%29#/media/File:Up_(2009_film).jpg",
	"https://www.youtube.com/watch?v=qas5lWp7_R0")
kung_fu_panda = media.Movie(
	"Kung Fu Panda",
	"Po and the rest of his Furious-Five gang defend ancient China from a villain",
	"https://en.wikipedia.org/wiki/Kung_Fu_Panda#/media/File:Kungfupanda.jpg",
	"https://www.youtube.com/watch?v=PXi3Mv6KMzY")
chicken_run = media.Movie(
	"Chicken Run",
	"A cocky American rooster saves the coup from turning into chicken pies",
	"https://en.wikipedia.org/wiki/Chicken_Run#/media/File:Chicken_run_ver1.jpg",
	"https://www.youtube.com/watch?v=jVdlxwX6A7g")
#dr_zhivago = media.Movie("Dr. Zhivago", "from Russia in early twentieth century", "https://en.wikipedia.org/wiki/Doctor_Zhivago_(film)#/media/File:DrZhivago_Asheet.jpg","https://www.youtube.com/watch?v=wAWrXTn5Www")
dr_zhivago = media.Movie(
	"Dr. Zhivago",
	"from Russia in early twentieth century",
	"https://upload.wikimedia.org/wikipedia/en/6/64/DrZhivago_Asheet.jpg",
	"https://www.youtube.com/watch?v=wAWrXTn5Www")
modern_times = media.Movie("Modern Times",
	"Charlie Chaplin illuminates industrialization",
	"https://en.wikipedia.org/wiki/Modern_Times_(film)#/media/File:Moderntimes.jpg",
	"https://www.youtube.com/watch?v=GLeDdzGUTq0")
ratatouille = media.Movie(
	"Rata Touille",
	"Story of Ratatouille",
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk")
movies = [toy_story, up,kung_fu_panda,chicken_run,dr_zhivago,\
	modern_times,ratatouille]

