import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // 1. Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        // 2. Declare variables (English Lesson)
        String adjective1; // description (e.g., fast, slow)
        String noun1;      // person, place, or thing
        String adjective2; // description
        String verb1;      // action (ending in -ing)
        String adjective3; // description

        // 3. Prompt user for input
        System.out.print("Enter an adjective (description): ");
        adjective1 = scanner.nextLine();

        System.out.print("Enter a noun (animal or person): ");
        noun1 = scanner.nextLine();

        System.out.print("Enter an adjective (description): ");
        adjective2 = scanner.nextLine();

        System.out.print("Enter a verb ending with -ing (action): ");
        verb1 = scanner.nextLine();

        System.out.print("Enter an adjective (description): ");
        adjective3 = scanner.nextLine();

        // 4. Output the story
        System.out.println("\nToday I went to a " + adjective1 + " zoo.");
        System.out.println("In an exhibit, I saw a " + noun1 + ".");
        System.out.println(noun1 + " was " + adjective2 + " and " + verb1 + "!");
        System.out.println("I was " + adjective3 + "!");

        // 5. Close the scanner
        scanner.close();
    }
}
