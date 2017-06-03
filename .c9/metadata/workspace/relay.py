{"changed":true,"filter":false,"title":"relay.py","tooltip":"/relay.py","value":"from cobe.brain import Brain\nimport datetime\nimport os.path\n\n#Import different classes\nimport sys\nsys.path.append('mongodb/')\nimport get\n\n'''\nPURPOSE: retrieve the brain from the cache and download it if it isn't\nMETHOD: Download from mongodb atlas database\nINPUT/OUTPUT: input is the uuid and output is the directory to the brain\n'''\ndef cache(uuid) :\n    directory = 'cache/' + uuid + '.brain'\n    #Check if it's in our cache\n    if os.path.exists(directory) :\n        #It exists in our cache\n        return directory\n    #download from database and put into cache\n    else :\n        get.cache(uuid)\n        return directory\n'''\nPURPOSE: to provide a chat relay for the chatbots\nMETHOD: Load brain from cache and query for message\nINPUT/OUTPUT: Inputs and output are similar where they are both in this format:\n    {\n        'uuid' : String - UUID\n        'message' : String - Message\n    }\n    \n    Creates the entry in a journal file\n'''\ndef chat(data) :\n    directory = cache(data['uuid'])\n    b = Brain(directory)\n    \n    reply = b.reply(data['message'])\n    \n    response = {\n        'message' : reply,\n        'uuid' : data['uuid'] \n    }\n    \n    #Log into our journal\n    \n    \n    return response\n\n'''\nPURPOSE: Create a log for the conversations\nMETHOD: Open up the journal file for the associated brain\nINPUT/OUPUT: The UUID for the brain, the message, and the brain response\n    Structure of journal file (identifier's are encapsulated by ``) -\n    [`DATETIME`] [`BRAIN OR USERNAME?`] : `REPLY`\n    \n    Example:\n    [2017-06-02 19:27:07] [BRAIN] : hello!\n    [2017-06-02 19:27:08] [hammadus] : hi!\n'''\ndef log(uuid, message, reply) :\n    #Directory of the brain journal\n    directory = 'cache/' + uuid + '.brain-journal'\n    \n    #Open journal\n    fp = open(directory, 'w')\n    \n    #Write to journal\n    fp.write('[' + str(datetime.datetime.now()) + '] ' + '[USER] : ' + message + '\\n')  #User message\n    fp.write('[' + str(datetime.datetime.now()) + '] ' + '[BRAIN] : ' + reply + '\\n')   #Brain message\n    \n    #Close journal and finalize\n    fp.close()","undoManager":{"mark":-22,"position":100,"stack":[[{"start":{"row":70,"column":71},"end":{"row":70,"column":72},"action":"insert","lines":["m"],"id":2901}],[{"start":{"row":70,"column":72},"end":{"row":70,"column":73},"action":"insert","lines":["e"],"id":2902}],[{"start":{"row":70,"column":73},"end":{"row":70,"column":74},"action":"insert","lines":["s"],"id":2903}],[{"start":{"row":70,"column":74},"end":{"row":70,"column":75},"action":"insert","lines":["s"],"id":2904}],[{"start":{"row":70,"column":75},"end":{"row":70,"column":76},"action":"insert","lines":["a"],"id":2905}],[{"start":{"row":70,"column":76},"end":{"row":70,"column":77},"action":"insert","lines":["g"],"id":2906}],[{"start":{"row":70,"column":77},"end":{"row":70,"column":78},"action":"insert","lines":["e"],"id":2907}],[{"start":{"row":70,"column":78},"end":{"row":70,"column":79},"action":"insert","lines":[" "],"id":2908}],[{"start":{"row":70,"column":79},"end":{"row":70,"column":80},"action":"insert","lines":["+"],"id":2909}],[{"start":{"row":70,"column":80},"end":{"row":70,"column":81},"action":"insert","lines":[" "],"id":2910}],[{"start":{"row":70,"column":81},"end":{"row":70,"column":83},"action":"insert","lines":["\"\""],"id":2911}],[{"start":{"row":70,"column":82},"end":{"row":70,"column":83},"action":"insert","lines":["\\"],"id":2912}],[{"start":{"row":70,"column":83},"end":{"row":70,"column":84},"action":"insert","lines":["n"],"id":2913}],[{"start":{"row":70,"column":84},"end":{"row":70,"column":85},"action":"remove","lines":["\""],"id":2914}],[{"start":{"row":70,"column":84},"end":{"row":70,"column":85},"action":"insert","lines":["'"],"id":2915}],[{"start":{"row":70,"column":81},"end":{"row":70,"column":82},"action":"remove","lines":["\""],"id":2916}],[{"start":{"row":70,"column":81},"end":{"row":70,"column":83},"action":"insert","lines":["''"],"id":2917}],[{"start":{"row":70,"column":82},"end":{"row":70,"column":83},"action":"remove","lines":["'"],"id":2918}],[{"start":{"row":70,"column":86},"end":{"row":70,"column":88},"action":"insert","lines":["  "],"id":2919}],[{"start":{"row":70,"column":87},"end":{"row":70,"column":88},"action":"remove","lines":[" "],"id":2920}],[{"start":{"row":70,"column":86},"end":{"row":70,"column":87},"action":"remove","lines":[" "],"id":2921}],[{"start":{"row":70,"column":86},"end":{"row":70,"column":87},"action":"insert","lines":[" "],"id":2922}],[{"start":{"row":70,"column":87},"end":{"row":70,"column":88},"action":"insert","lines":["#"],"id":2923}],[{"start":{"row":70,"column":88},"end":{"row":70,"column":89},"action":"insert","lines":["F"],"id":2924}],[{"start":{"row":70,"column":89},"end":{"row":70,"column":90},"action":"insert","lines":["o"],"id":2925}],[{"start":{"row":70,"column":90},"end":{"row":70,"column":91},"action":"insert","lines":["r"],"id":2926}],[{"start":{"row":70,"column":91},"end":{"row":70,"column":92},"action":"insert","lines":[" "],"id":2927}],[{"start":{"row":70,"column":92},"end":{"row":70,"column":93},"action":"insert","lines":["t"],"id":2928}],[{"start":{"row":70,"column":92},"end":{"row":70,"column":93},"action":"remove","lines":["t"],"id":2929}],[{"start":{"row":70,"column":91},"end":{"row":70,"column":92},"action":"remove","lines":[" "],"id":2930}],[{"start":{"row":70,"column":90},"end":{"row":70,"column":91},"action":"remove","lines":["r"],"id":2931}],[{"start":{"row":70,"column":89},"end":{"row":70,"column":90},"action":"remove","lines":["o"],"id":2932}],[{"start":{"row":70,"column":88},"end":{"row":70,"column":89},"action":"remove","lines":["F"],"id":2933}],[{"start":{"row":70,"column":88},"end":{"row":70,"column":89},"action":"insert","lines":["U"],"id":2934}],[{"start":{"row":70,"column":89},"end":{"row":70,"column":90},"action":"insert","lines":["s"],"id":2935}],[{"start":{"row":70,"column":90},"end":{"row":70,"column":91},"action":"insert","lines":["e"],"id":2936}],[{"start":{"row":70,"column":91},"end":{"row":70,"column":92},"action":"insert","lines":["r"],"id":2937}],[{"start":{"row":70,"column":92},"end":{"row":70,"column":93},"action":"insert","lines":[" "],"id":2938}],[{"start":{"row":70,"column":93},"end":{"row":70,"column":94},"action":"insert","lines":["m"],"id":2939}],[{"start":{"row":70,"column":94},"end":{"row":70,"column":95},"action":"insert","lines":["e"],"id":2940}],[{"start":{"row":70,"column":95},"end":{"row":70,"column":96},"action":"insert","lines":["s"],"id":2941}],[{"start":{"row":70,"column":96},"end":{"row":70,"column":97},"action":"insert","lines":["s"],"id":2942}],[{"start":{"row":70,"column":97},"end":{"row":70,"column":98},"action":"insert","lines":["a"],"id":2943}],[{"start":{"row":70,"column":98},"end":{"row":70,"column":99},"action":"insert","lines":["g"],"id":2944}],[{"start":{"row":70,"column":99},"end":{"row":70,"column":100},"action":"insert","lines":["e"],"id":2945}],[{"start":{"row":70,"column":100},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":2946},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":71,"column":4},"end":{"row":71,"column":100},"action":"insert","lines":["fp.write('[' + str(datetime.datetime.now()) + '] ' + '[USER] : ' + message + '\\n') #User message"],"id":2947}],[{"start":{"row":71,"column":90},"end":{"row":71,"column":91},"action":"remove","lines":["e"],"id":2948}],[{"start":{"row":71,"column":89},"end":{"row":71,"column":90},"action":"remove","lines":["s"],"id":2949}],[{"start":{"row":71,"column":88},"end":{"row":71,"column":89},"action":"remove","lines":["U"],"id":2950}],[{"start":{"row":71,"column":88},"end":{"row":71,"column":89},"action":"remove","lines":["r"],"id":2951}],[{"start":{"row":71,"column":88},"end":{"row":71,"column":89},"action":"insert","lines":["B"],"id":2952}],[{"start":{"row":71,"column":89},"end":{"row":71,"column":90},"action":"insert","lines":["r"],"id":2953}],[{"start":{"row":71,"column":90},"end":{"row":71,"column":91},"action":"insert","lines":["a"],"id":2954}],[{"start":{"row":71,"column":91},"end":{"row":71,"column":92},"action":"insert","lines":["i"],"id":2955}],[{"start":{"row":71,"column":92},"end":{"row":71,"column":93},"action":"insert","lines":["n"],"id":2956}],[{"start":{"row":71,"column":77},"end":{"row":71,"column":78},"action":"remove","lines":["e"],"id":2957}],[{"start":{"row":71,"column":76},"end":{"row":71,"column":77},"action":"remove","lines":["g"],"id":2958}],[{"start":{"row":71,"column":75},"end":{"row":71,"column":76},"action":"remove","lines":["a"],"id":2959}],[{"start":{"row":71,"column":74},"end":{"row":71,"column":75},"action":"remove","lines":["s"],"id":2960}],[{"start":{"row":71,"column":73},"end":{"row":71,"column":74},"action":"remove","lines":["s"],"id":2961}],[{"start":{"row":71,"column":72},"end":{"row":71,"column":73},"action":"remove","lines":["e"],"id":2962}],[{"start":{"row":71,"column":71},"end":{"row":71,"column":72},"action":"remove","lines":["m"],"id":2963}],[{"start":{"row":71,"column":71},"end":{"row":71,"column":72},"action":"insert","lines":["r"],"id":2964}],[{"start":{"row":71,"column":72},"end":{"row":71,"column":73},"action":"insert","lines":["e"],"id":2965}],[{"start":{"row":71,"column":73},"end":{"row":71,"column":74},"action":"insert","lines":["p"],"id":2966}],[{"start":{"row":71,"column":74},"end":{"row":71,"column":75},"action":"insert","lines":["l"],"id":2967}],[{"start":{"row":71,"column":75},"end":{"row":71,"column":76},"action":"insert","lines":["y"],"id":2968}],[{"start":{"row":71,"column":62},"end":{"row":71,"column":63},"action":"remove","lines":["R"],"id":2969}],[{"start":{"row":71,"column":61},"end":{"row":71,"column":62},"action":"remove","lines":["E"],"id":2970}],[{"start":{"row":71,"column":60},"end":{"row":71,"column":61},"action":"remove","lines":["S"],"id":2971}],[{"start":{"row":71,"column":59},"end":{"row":71,"column":60},"action":"remove","lines":["U"],"id":2972}],[{"start":{"row":71,"column":59},"end":{"row":71,"column":60},"action":"insert","lines":["B"],"id":2973}],[{"start":{"row":71,"column":60},"end":{"row":71,"column":61},"action":"insert","lines":["R"],"id":2974}],[{"start":{"row":71,"column":61},"end":{"row":71,"column":62},"action":"insert","lines":["A"],"id":2975}],[{"start":{"row":71,"column":62},"end":{"row":71,"column":63},"action":"insert","lines":["I"],"id":2976}],[{"start":{"row":71,"column":63},"end":{"row":71,"column":64},"action":"insert","lines":["N"],"id":2977}],[{"start":{"row":70,"column":86},"end":{"row":70,"column":87},"action":"remove","lines":[" "],"id":2978}],[{"start":{"row":70,"column":86},"end":{"row":70,"column":88},"action":"insert","lines":["  "],"id":2979}],[{"start":{"row":71,"column":85},"end":{"row":71,"column":86},"action":"remove","lines":[" "],"id":2980}],[{"start":{"row":71,"column":85},"end":{"row":71,"column":88},"action":"insert","lines":["   "],"id":2981}],[{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"insert","lines":["n"],"id":2982}],[{"start":{"row":56,"column":33},"end":{"row":56,"column":34},"action":"insert","lines":["a"],"id":2983}],[{"start":{"row":56,"column":33},"end":{"row":56,"column":34},"action":"remove","lines":["a"],"id":2984}],[{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"remove","lines":["n"],"id":2985}],[{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"insert","lines":["N"],"id":2986}],[{"start":{"row":56,"column":33},"end":{"row":56,"column":34},"action":"insert","lines":["A"],"id":2987}],[{"start":{"row":56,"column":34},"end":{"row":56,"column":35},"action":"insert","lines":["M"],"id":2988}],[{"start":{"row":56,"column":35},"end":{"row":56,"column":36},"action":"insert","lines":["E"],"id":2989}],[{"start":{"row":60,"column":30},"end":{"row":60,"column":31},"action":"remove","lines":["R"],"id":2990}],[{"start":{"row":60,"column":29},"end":{"row":60,"column":30},"action":"remove","lines":["E"],"id":2991}],[{"start":{"row":60,"column":28},"end":{"row":60,"column":29},"action":"remove","lines":["S"],"id":2992}],[{"start":{"row":60,"column":27},"end":{"row":60,"column":28},"action":"remove","lines":["U"],"id":2993}],[{"start":{"row":60,"column":27},"end":{"row":60,"column":28},"action":"insert","lines":["h"],"id":2994}],[{"start":{"row":60,"column":28},"end":{"row":60,"column":29},"action":"insert","lines":["a"],"id":2995}],[{"start":{"row":60,"column":29},"end":{"row":60,"column":30},"action":"insert","lines":["m"],"id":2996}],[{"start":{"row":60,"column":30},"end":{"row":60,"column":31},"action":"insert","lines":["m"],"id":2997}],[{"start":{"row":60,"column":31},"end":{"row":60,"column":32},"action":"insert","lines":["a"],"id":2998}],[{"start":{"row":60,"column":32},"end":{"row":60,"column":33},"action":"insert","lines":["d"],"id":2999}],[{"start":{"row":60,"column":33},"end":{"row":60,"column":34},"action":"insert","lines":["u"],"id":3000}],[{"start":{"row":60,"column":34},"end":{"row":60,"column":35},"action":"insert","lines":["s"],"id":3001}]]},"ace":{"folds":[],"scrolltop":797,"scrollleft":0,"selection":{"start":{"row":73,"column":31},"end":{"row":73,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1496431852048}