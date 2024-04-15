# Youtube Python Comments Crawler
## Requirements
- Youtube API
- Google-api-python-client
## How To Get Youtube API
You could get it by accessing Google Developers Console or visit the link below for the complete tutorial:
> https://developers.google.com/youtube/v3/getting-started
## Google Api Python Client
Install it using pip
> <code>pip install google-api-python-client</code>
## How To Run
This app using using argparse, so you have to pass a few args:
<table>
  <th>Args<th>Vars<th>Information<th>Example</th>
  <tr>
    <td>--api_path<td>API_PATH<td>Your API File Path<td>"C:\Users\JohnDoe\Documents\Projects\yourapikey.txt"</td>
  <tr>
    <td>--video_id<td>VIDEO_ID<td>Youtube Video ID<td>If the URL is "https://www.youtube.com/watch?v=dQw4w9WgXcQ", the video ID is "dQw4w9WgXcQ".</td>
  <tr>
    <td>--max_results<td>MAX_RESULTS<td>Max Results Comments<td>100</td>
  <tr>
    <td>--output<td>OUTPUT<td>Output File Name<td>"Comments" (The program will add ".csv" automatically)</td>
</table>
To run simply run this command in command prompt
<br>
<code>python comments_crawler.py --api_path "your_api_path" --video_id "video_id" --max_results "max_results" --output "output file name"</code>

