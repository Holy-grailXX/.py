import java.util.List;

public class Change {

    record Person(String name, int age) {}

    public static void main(String[] args) {
        List<Person> domain = List.of(
            new Person("Emmanuel", 34),
            new Person("omar", 35),
            new Person("Mofi", 18),
            new Person("Greg", 20)
        );
    }
}
    