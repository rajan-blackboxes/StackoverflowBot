# StackoverflowBot
Scrape and create dataset for specific tagged language in stackoverflow

# How to use  
After cloning this repo and  changing directory to `StackoverflowBot`, follow below guidelines

1. First , Create virtual environment and install required libraries using following code
    ```
   python -m venv Stackbot
   source Stackbot/bin/activate 
   pip install -r requirements.txt
   ```    
2. Now run code on command line as  
  `python main.py -lang python -max_page 20 -o python_scraped.json`    
   where,  
        **-lang**: *Tagged language of stackoverflow. e.g python, c++, javascript*  
        **-max_page**: *Maximum pagination of given language, should not be greater than actual*  
        **-o**: *output file name, can be json or csv e.g some_scraped.json*  

3. If any error occurs, Please feel free to ask on issues,  
 or comment all lines below *#logs* in `settings.py` to debug yourself.
 
# dataset details
It scrapes following things,

- *question_vote_count: Number of votes of that question*
- *question_answer_count: Answer counts of that question*
- *question_title: Title of question*
- *question_title_link: Url link of that question*
- *question_tags = Tags of that question*

  
