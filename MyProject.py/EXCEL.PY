import pandas as pd
import numpy as np
dict1={
    "email":["nazishcs@iul.ac.in","farheenpa@stu dent.iul.ac.in","rajpatel@student.iul.ac.in","iqrarahma@student.iul.ac.in","khaaquib@student.iul.ac.in","aypandey@student.iul.ac.in","contactbe@iul.ac.in","nazirakh@student.iul.ac.in","nesarah@iul.ac.in","kushagraa@student.iul.ac.in","shabihkh@student.iul.ac.in","danishrr@student.iul.ac.in"],
    "name":["najish mam","farheen","raj","iqrar","aqib","aayushi","bilal","najira","nesar","kushagra","sabhi","danish raj"],
    "number":["+917275930529","+916201131905","+919076933318","+918948705723","+917379402191","+919044293407","+916386164834","+917234828651","+919670948102","+919235573653","+919084457080","+918979248180"]

}
df=pd.DataFrame(dict1)
df.to_csv("school.csv",index=False)