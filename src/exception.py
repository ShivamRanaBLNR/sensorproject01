import sys
#sys...module whichg will interact with my python interpreter



def error_message_detail(error,error_detail:sys):
    print(error_detail)
    print(error_detail.exc_info())
    _,_,exc_tb=error_detail.exc_info()
    #hum thied info capture kr reh exc_tb variable me////traceback object..isme hi line no file name sb capture hote h
    
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    error_message="Error occured python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    
    return error_message





#ou can also consider using the traceback module for more flexibility in formatting exception traces:



class CustomException(Exception):
    #from base exception
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        #base class se sari properties inherit kr rhe
        self.error_message=error_message_detail(
            error_message,error_detail=error_detail
        )
        
        
    #to display message
    def __str__(self):
        return self.error_message