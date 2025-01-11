from typing import List
from src.decorators.catch import catch
from src.exceptions.wrong_arguments_number_exception import WrongArgumentsNumberException
from src.models.organizer import note_book


@catch
def find_tags(args: List[str]):
    if len(args) != 1:
        WrongArgumentsNumberException(1)
    
    search_tag = args[0]
    result = note_book.find_tags(search_tag)
    if len(result) != 0:
        print(result)
    else:
        print(f"Nothing found with this tag - {search_tag}")
    
    
    

