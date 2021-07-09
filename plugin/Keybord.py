keybord1= InlineKeyboardMarkup( [
        [ 
            InlineKeyboardButton("Afrikaans", callback_data='af'),
             InlineKeyboardButton("Albanian", callback_data='sq'),
            InlineKeyboardButton("Amharic",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Arabic", callback_data='ar'),
        InlineKeyboardButton("Armenian", callback_data='hy'),      
        InlineKeyboardButton("Azerbaijani",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Basque",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusian",callback_data ="be"),       	
	InlineKeyboardButton("Bengali",callback_data="bn")],
	
	[InlineKeyboardButton("Bosnian",callback_data = "bs"),
	InlineKeyboardButton("Bulgarian",callback_data ="bg"),
	InlineKeyboardButton("Catalan",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Corsican",callback_data ="co"),
	InlineKeyboardButton("Croatian",callback_data = "hr"),
	InlineKeyboardButton("Czech", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danish",callback_data = "da"),
	InlineKeyboardButton("Dutch",callback_data = "nl"),
	InlineKeyboardButton("Esperanto",callback_data = "eo"),	 
	],
	[InlineKeyboardButton(" Next --->",callback_data = "page2")
	]
	] )

keybord2= InlineKeyboardMarkup([
           [InlineKeyboardButton("English",callback_data = "en"),
           InlineKeyboardButton("Estonian",callback_data = "et"),
           InlineKeyboardButton("Finnish",callback_data = "fi")
           ],
           [InlineKeyboardButton("French",callback_data = "fr"),
           InlineKeyboardButton("Frisian",callback_data = "fy"),
           InlineKeyboardButton("Galician",callback_data = "gl")
           ],
           [InlineKeyboardButton("Georgian",callback_data = "ka"),
           InlineKeyboardButton("German",callback_data = "de"),
           InlineKeyboardButton("Greek",callback_data = "el")
           ],
           [InlineKeyboardButton("Gujarati",callback_data = "gu"),
           InlineKeyboardButton("Haitian Creole",callback_data = "ht"),
           InlineKeyboardButton("Hausa",callback_data ="ha")
           ],
           [InlineKeyboardButton("Hindi",callback_data = "hi"),
           InlineKeyboardButton("Hungarian",callback_data = "hu"),
           InlineKeyboardButton("Icelandic",callback_data = "is")
           ],
           [InlineKeyboardButton("Igbo",callback_data = "ig"),
           InlineKeyboardButton("Indonesian",callback_data = "id"),
           InlineKeyboardButton("Irish",callback_data = "ga")
           ],
           [InlineKeyboardButton("<--- Back",callback_data = "page1"),
           InlineKeyboardButton(" Next --->",callback_data = "page3"),
           ]
            ])
		
keybord3 = InlineKeyboardMarkup([
                [ InlineKeyboardButton("Italian",callback_data = "it"),
                InlineKeyboardButton("Japanese",callback_data = "ja"),
                InlineKeyboardButton("Javanese",callback_data = "jv")
                ],
                [InlineKeyboardButton("Kannada",callback_data = "kn"),
                InlineKeyboardButton("Kazakh",callback_data = "kk"),
                InlineKeyboardButton("Khmer",callback_data = "km")
                ],
                [InlineKeyboardButton("Kinyarwanda",callback_data = "rw"),
                InlineKeyboardButton("Korean",callback_data ="ko"),
                InlineKeyboardButton("Kurdish",callback_data = "ku")
                ],
                [ InlineKeyboardButton("Kyrgyz",callback_data ="ky"),
                InlineKeyboardButton("Lao",callback_data = "lo"),
                InlineKeyboardButton("Latin",callback_data = "la")
                ],
                [InlineKeyboardButton("Latvian",callback_data = "lv"),
                InlineKeyboardButton('Lithuanian',callback_data ="lt"),
                InlineKeyboardButton("Luxembourgish",callback_data = "lb")
                ],
                [InlineKeyboardButton("Macedonian",callback_data = "mk"),
                InlineKeyboardButton("Malagasy",callback_data ="mg"),
                InlineKeyboardButton("Malay",callback_data ="ms")
                ],
                [InlineKeyboardButton("<--- Back",callback_data = "page2"),
                InlineKeyboardButton(" Next --->",callback_data = "page4")
                ]
              
 
 ])

