package Observer;

import Observer.Impls.ChannelSubscriber;
import Observer.Impls.YouTubeChannel;

public class ObserverPattern {
    public static void main(String[] args) {
        YouTubeChannel channel = new YouTubeChannel("Tech Insights");

        ChannelSubscriber subscriber1 = new ChannelSubscriber("Alice");
        ChannelSubscriber subscriber2 = new ChannelSubscriber("Bob");

        channel.subscribe(subscriber1);
        channel.subscribe(subscriber2);

        channel.uploadVideo("Design Patterns in Java", "Java");

        channel.unsubscribe(subscriber1);

        channel.uploadVideo("Observer Pattern Explained", "Java");
    }
}
