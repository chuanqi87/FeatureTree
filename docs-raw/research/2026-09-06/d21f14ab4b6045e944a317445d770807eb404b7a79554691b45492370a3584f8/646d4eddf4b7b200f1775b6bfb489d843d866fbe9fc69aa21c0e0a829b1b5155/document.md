# Smart reply

![](/static/ml-kit/images/smart_reply2x.png)

With ML Kit's smart reply API, you can automatically generate relevant
replies to messages. Smart reply helps your users respond to messages quickly,
and makes it easier to reply to messages on devices with limited input
capabilities.

[iOS](https://developers.google.com/ml-kit/language/smart-reply/ios)
[Android](https://developers.google.com/ml-kit/language/smart-reply/android)

## Key capabilities

* The smart reply model generates reply suggestions based on the full context
  of a conversation, not just a single message. This means the suggestions
  are more helpful to your users.
* The on-device model generates replies quickly and doesn't require you to
  send users' messages to a remote server.

## Limitations

* Smart reply is intended for casual conversations in consumer apps. Reply
  suggestions might not be appropriate for other contexts or audiences.
* Currently, only English is supported. The model automatically identifies the
  language being used and only provides suggestions when it's English.

## How the model works

* The model uses up to 10 of the most recent messages from a conversation
  history to generate reply suggestions.
* It detects the language of the conversation and only attempts to provide
  responses when the language is determined to be English.
* The model compares the messages against a list of sensitive topics and
  won’t provide suggestions when it detects a sensitive topic.
* If the language is determined to be English and no sensitive topics are
  detected, the model provides up to three suggested responses. The number of
  responses depends on how many meet a sufficient level of confidence based on
  the input to the model.

## Provide feedback

Due to the complexity of natural language processing, the suggestions provided
by the model may not be appropriate for all contexts or audiences. If you
encounter inappropriate reply suggestions, reach out to
[ML Kit support](https://developers.google.com/ml-kit/community). Your feedback
helps to improve the model and the filters for sensitive topics.

## Example results

### Input

| Timestamp | User ID | Local User? | Message |
| --- | --- | --- | --- |
| Thu Feb 21 13:13:39 PST 2019 |  | true | are you on your way? |
| Thu Feb 21 13:15:03 PST 2019 | FRIEND0 | false | Running late, sorry! |

### Suggested replies

| Suggestion #1 | Suggestion #2 | Suggestion #3 |
| --- | --- | --- |
| No worries | 😞 | No problem! |
