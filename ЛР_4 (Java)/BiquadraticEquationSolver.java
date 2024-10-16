import java.util.Scanner;

public class BiquadraticEquationSolver {

    public static void solve(double a, double b, double c) {
        System.out.printf("Уравнение: (%.1f)x^4 + (%.1f)x^2 + (%.1f) = 0%n", a, b, c);

        double D = b * b - 4 * a * c;
        System.out.printf("Дискриминант: %.2f%n", D);

        if (D < 0) {
            System.out.println("Корней нет.");
        } else if (D == 0) {
            double y = -b / (2 * a);
            if (y < 0) {
                System.out.println("Корней нет.");
            } else {
                double x = Math.sqrt(y);
                printRoot(1, x);
                if (x != 0) {
                    printRoot(2, -x);
                }
            }
        } else {
            double sqrtD = Math.sqrt(D);
            double y1 = (-b + sqrtD) / (2 * a);
            double y2 = (-b - sqrtD) / (2 * a);

            int rootCount = 1;

            if (y1 >= 0) {
                double x1 = Math.sqrt(y1);
                printRoot(rootCount++, x1);
                if (x1 != 0) {
                    printRoot(rootCount++, -x1);
                }
            }
            if (y2 >= 0) {
                double x2 = Math.sqrt(y2);
                printRoot(rootCount++, x2);
                printRoot(rootCount++, -x2);
            }
        }
    }

    private static void printRoot(int rootNumber, double root) {
        if (root != -0 & root != 0) {
            System.out.printf("Корень %d = %.2f%n", rootNumber, root);
        }
        else {
            root = 0;
            System.out.printf("Корень %d = %.2f%n", rootNumber, root);
        }
    }

    public static void main(String[] args) {
        double a = getK(args, 0, "Введите коэффициент A: ");
        double b = getK(args, 1, "Введите коэффициент B: ");
        double c = getK(args, 2, "Введите коэффициент C: ");

        solve(a, b, c);
    }

    private static double getK(String[] args, int index, String prompt) {
        if (args.length > index) {
            try {
                return Double.parseDouble(args[index]);
            } catch (NumberFormatException e) {
                System.out.println("Некорректное значение для коэффициента " + prompt);
            }
        }

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print(prompt);
            try {
                return Double.parseDouble(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Некорректное значение. Попробуйте снова.");
            }
        }
    }
}
