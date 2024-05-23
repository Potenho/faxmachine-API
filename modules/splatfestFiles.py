from decouple import config
import modules.byml as byml
import dateparser
import datetime


class SplatfestFiles():
    


    def get_dict(path:str = "public/splatfestFiles/00000544") -> dict:

        file = open(path, "rb")
                
        content = byml.Byml(file.read())
            
        file.close()
        

        return content.parse()
    
    def saveFile(content:dict, path:str = "Test") -> None:

        with open(path, "wb") as fest_file:
            writer = byml.Writer(content, be=True, version=1)
            writer.write(fest_file)
            fest_file.close()   


    def date_from_str(date:str) -> datetime.datetime:

        return dateparser.parse(date)

