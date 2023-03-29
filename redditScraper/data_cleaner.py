import constants
import json


# this function takes the raw reddit post information and creates a
def clean_dataset(self):
    list_of_posts = []
    for sub in constants.settings.SUBREDDITS:
        for post_key in self[sub]:
            current_sub = self.get(sub)
            current_post = current_sub.get(post_key)
            title = current_post["Title"]
            date = current_post["date_posted"]
            post = current_post["Post"]
            comments = [current_post["Comments"]]
            json_comments = json.dumps(comments)
            entry = dict({"subreddit": sub, "post_title": title, "date_posted": date, "post_content": post, "comments": json_comments})
            list_of_posts.append(entry)
    return list_of_posts
