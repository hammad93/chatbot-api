{"changed":true,"filter":false,"title":"upload.py","tooltip":"/create-bot/upload.py","value":"'''\nHammad Usmani\nLast Updated: 5/1/17\n\nUPLOAD BRAIN\n\nPURPOSE: Upload the markov chain chatbot stored in a .brain file\nMETHOD: Use the MongoDB Atlas driver to connect to the cloud instance and upload\nusing gridfs. This includes any metadata associated with the file.\nINPUT: .brain file  \nOUTPUT: Stored .brain in the database\nReferences:\n- https://docs.mongodb.com/manual/reference/connection-string/\n- https://docs.atlas.mongodb.com/driver-connection/#python-driver-example\n\n'''\n","undoManager":{"mark":92,"position":100,"stack":[[{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["t"],"id":346}],[{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["a"],"id":347}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":[" "],"id":348}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"remove","lines":[" "],"id":349}],[{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["d"],"id":350}],[{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["a"],"id":351}],[{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["t"],"id":352}],[{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":["a"],"id":353}],[{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":[" "],"id":354}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["a"],"id":355}],[{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["s"],"id":356}],[{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["s"],"id":357}],[{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["o"],"id":358}],[{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["c"],"id":359}],[{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["i"],"id":360}],[{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["a"],"id":361}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["t"],"id":362}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["e"],"id":363}],[{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["d"],"id":364}],[{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":[" "],"id":365}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["w"],"id":366}],[{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["i"],"id":367}],[{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["t"],"id":368}],[{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["h"],"id":369}],[{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"insert","lines":[" "],"id":370}],[{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"insert","lines":["t"],"id":371}],[{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"insert","lines":["h"],"id":372}],[{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"insert","lines":[" "],"id":373},{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"remove","lines":["e"],"id":374}],[{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"remove","lines":[" "],"id":375}],[{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"insert","lines":["e"],"id":376}],[{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":[" "],"id":377}],[{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["f"],"id":378}],[{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["i"],"id":379}],[{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["l"],"id":380}],[{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"insert","lines":["e"],"id":381}],[{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"insert","lines":["."],"id":382}],[{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"remove","lines":["."],"id":383}],[{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"insert","lines":["."],"id":384}],[{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":[" "],"id":385}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["."],"id":386}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["b"],"id":387}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["r"],"id":388}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["a"],"id":389}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["i"],"id":390}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["n"],"id":391}],[{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":[" "],"id":392}],[{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["f"],"id":393}],[{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["i"],"id":394}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["l"],"id":395}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["e"],"id":396}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":[" "],"id":397}],[{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":[" "],"id":398}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["S"],"id":399}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["t"],"id":400}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["o"],"id":401}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["r"],"id":402}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["e"],"id":403}],[{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["d"],"id":404}],[{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":[" "],"id":405}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["."],"id":406}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["r"],"id":407}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"remove","lines":["r"],"id":408}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["b"],"id":409}],[{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["r"],"id":410}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["a"],"id":411}],[{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["i"],"id":412}],[{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["n"],"id":413}],[{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":[" "],"id":414}],[{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["i"],"id":415}],[{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["n"],"id":416}],[{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":[" "],"id":417}],[{"start":{"row":10,"column":25},"end":{"row":10,"column":26},"action":"insert","lines":["t"],"id":418}],[{"start":{"row":10,"column":26},"end":{"row":10,"column":27},"action":"insert","lines":["h"],"id":419}],[{"start":{"row":10,"column":27},"end":{"row":10,"column":28},"action":"insert","lines":["e"],"id":420}],[{"start":{"row":10,"column":28},"end":{"row":10,"column":29},"action":"insert","lines":[" "],"id":421}],[{"start":{"row":10,"column":29},"end":{"row":10,"column":30},"action":"insert","lines":["f"],"id":422}],[{"start":{"row":10,"column":30},"end":{"row":10,"column":31},"action":"insert","lines":["a"],"id":423}],[{"start":{"row":10,"column":30},"end":{"row":10,"column":31},"action":"remove","lines":["a"],"id":424}],[{"start":{"row":10,"column":29},"end":{"row":10,"column":30},"action":"remove","lines":["f"],"id":425}],[{"start":{"row":10,"column":29},"end":{"row":10,"column":30},"action":"insert","lines":["d"],"id":426}],[{"start":{"row":10,"column":30},"end":{"row":10,"column":31},"action":"insert","lines":["a"],"id":427}],[{"start":{"row":10,"column":31},"end":{"row":10,"column":32},"action":"insert","lines":["t"],"id":428}],[{"start":{"row":10,"column":32},"end":{"row":10,"column":33},"action":"insert","lines":["a"],"id":429}],[{"start":{"row":10,"column":33},"end":{"row":10,"column":34},"action":"insert","lines":["b"],"id":430}],[{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"insert","lines":["a"],"id":431}],[{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"insert","lines":["s"],"id":432}],[{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"insert","lines":["e"],"id":433}],[{"start":{"row":11,"column":11},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":434}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["-"],"id":435}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":[" "],"id":436}],[{"start":{"row":12,"column":2},"end":{"row":12,"column":62},"action":"insert","lines":["https://docs.mongodb.com/manual/reference/connection-string/"],"id":437}],[{"start":{"row":12,"column":62},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":438}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["-"],"id":439}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":[" "],"id":440}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":73},"action":"insert","lines":["https://docs.atlas.mongodb.com/driver-connection/#python-driver-example"],"id":441}],[{"start":{"row":13,"column":73},"end":{"row":13,"column":74},"action":"insert","lines":["."],"id":442}],[{"start":{"row":13,"column":73},"end":{"row":13,"column":74},"action":"remove","lines":["."],"id":443}],[{"start":{"row":13,"column":66},"end":{"row":13,"column":73},"action":"remove","lines":["example"],"id":444},{"start":{"row":13,"column":66},"end":{"row":13,"column":73},"action":"insert","lines":["example"]}],[{"start":{"row":13,"column":66},"end":{"row":13,"column":73},"action":"remove","lines":["example"],"id":445},{"start":{"row":13,"column":66},"end":{"row":13,"column":73},"action":"insert","lines":["example"]}],[{"start":{"row":13,"column":73},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":446}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":0},"end":{"row":14,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1493668341119}