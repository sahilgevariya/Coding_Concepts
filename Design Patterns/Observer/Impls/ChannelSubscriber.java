package Observer.Impls;

import Observer.interfaces.Observer;
import Observer.models.VideoEvent;

public class ChannelSubscriber implements Observer<VideoEvent> {
    private String subscriberName;

    public ChannelSubscriber(String subscriberName) {
        this.subscriberName = subscriberName;
    }

    @Override
    public void update(VideoEvent event) {
        System.out.println(subscriberName + " received notification: New video uploaded on " + event.channelName() +
                " - Title: " + event.videoTitle() + ", Description: " + event.videoDescription());
    }
}
