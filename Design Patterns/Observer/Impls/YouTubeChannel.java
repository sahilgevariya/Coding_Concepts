package Observer.Impls;

import Observer.models.VideoEvent;

public class YouTubeChannel extends Observable<VideoEvent> {
    private String channelName;

    public YouTubeChannel(String channelName) {
        this.channelName = channelName;
    }

    public void uploadVideo(String title, String description) {
        VideoEvent event = new VideoEvent(channelName, title, description);
        notifyObservers(event);
    }
}
