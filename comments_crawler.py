from googleapiclient.discovery import build
import pandas
import argparse

"""
Made by Edwin Jaya
Simple Youtube Comments Crawler
"""

class CommentsCrawler:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="Youtube Comments Crawler by Edwin Jaya")
        parser.add_argument("--api_path", type=str, help="Your API File Path",required=True)
        parser.add_argument("--video_id", type=str, help="Youtube Video ID",required=True)
        parser.add_argument("--max_results", type=int, help="Max Results Comments",required=True)
        parser.add_argument("--output", type=str, help="Output File Name",required=True)
        arg = parser.parse_args()
        api = arg.api_path
        self.api_key = self.load_api(api)
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        comments = self.get_comments(arg.video_id, arg.max_results)
        data = self.create_df(comments)
        self.save_dataframe(data, arg.output + ".csv")
        
        
    def save_dataframe(self,data:pandas.DataFrame, filename:str)->None:
        try:
            data.to_csv(filename, index=False)
            print("Dataframe saved successfully")
        except Exception as e:
            print("Error: ", e)
            
    def load_api(self, api:str)->str:
        try:
            with open(api, 'r') as file:
                api_key = file.read()
        except FileNotFoundError as e:
            print("Error: API file not found -", e)
            api_key = None
        
        return api_key
    
    def get_comments(self, video_id:str,max_results:int)->list:
        comments = []
        try:
            request = self.youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=max_results,
                textFormat="plainText"
            )

            response = request.execute()

            for item in response["items"]:
                comment_text = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
                comments.append(comment_text)
                
            print("Successfully Collected Comments: ", len(comments))
            return comments
        except Exception as e:
            print("Error: ", e)
            
    def create_df(self, comments:list)->pandas.DataFrame:
        data = pandas.DataFrame(comments, columns=["Comments"])
        return data
    
if __name__ == "__main__":
    CommentsCrawler()