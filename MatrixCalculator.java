//simple matrix calculator in Java that supports addition, subtraction, multiplication, and scalar multiplication operations
import java.util.Scanner;

public class MatrixCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Matrix Calculator");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Scalar Multiplication");

        System.out.print("Enter your choice: ");
        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                performAddition(scanner);
                break;
            case 2:
                performSubtraction(scanner);
                break;
            case 3:
                performMultiplication(scanner);
                break;
            case 4:
                performScalarMultiplication(scanner);
                break;
            default:
                System.out.println("Invalid choice");
        }

        scanner.close();
    }

    public static void performAddition(Scanner scanner) {
        double[][] matrixA = readMatrix(scanner, "A");
        double[][] matrixB = readMatrix(scanner, "B");

        if (!areDimensionsValid(matrixA, matrixB)) {
            System.out.println("Matrices must have the same dimensions for addition.");
            return;
        }

        double[][] result = new double[matrixA.length][matrixA[0].length];

        for (int i = 0; i < matrixA.length; i++) {
            for (int j = 0; j < matrixA[0].length; j++) {
                result[i][j] = matrixA[i][j] + matrixB[i][j];
            }
        }

        System.out.println("Result:");
        printMatrix(result);
    }

    public static void performSubtraction(Scanner scanner) {
        double[][] matrixA = readMatrix(scanner, "A");
        double[][] matrixB = readMatrix(scanner, "B");

        if (!areDimensionsValid(matrixA, matrixB)) {
            System.out.println("Matrices must have the same dimensions for subtraction.");
            return;
        }

        double[][] result = new double[matrixA.length][matrixA[0].length];

        for (int i = 0; i < matrixA.length; i++) {
            for (int j = 0; j < matrixA[0].length; j++) {
                result[i][j] = matrixA[i][j] - matrixB[i][j];
            }
        }

        System.out.println("Result:");
        printMatrix(result);
    }

    public static void performMultiplication(Scanner scanner) {
        double[][] matrixA = readMatrix(scanner, "A");
        double[][] matrixB = readMatrix(scanner, "B");

        if (matrixA[0].length != matrixB.length) {
            System.out.println("Invalid dimensions for matrix multiplication.");
            return;
        }

        double[][] result = new double[matrixA.length][matrixB[0].length];

        for (int i = 0; i < matrixA.length; i++) {
            for (int j = 0; j < matrixB[0].length; j++) {
                for (int k = 0; k < matrixA[0].length; k++) {
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        System.out.println("Result:");
        printMatrix(result);
    }

    public static void performScalarMultiplication(Scanner scanner) {
        double[][] matrix = readMatrix(scanner, "A");

        System.out.print("Enter the scalar value: ");
        double scalar = scanner.nextDouble();

        double[][] result = new double[matrix.length][matrix[0].length];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                result[i][j] = matrix[i][j] * scalar;
            }
        }

        System.out.println("Result:");
        printMatrix(result);
    }

    public static double[][] readMatrix(Scanner scanner, String matrixName) {
        System.out.print("Enter the number of rows for matrix " + matrixName + ": ");
        int rows = scanner.nextInt();
        System.out.print("Enter the number of columns for matrix " + matrixName + ": ");
        int cols = scanner.nextInt();

        double[][] matrix = new double[rows][cols];
        System.out.println("Enter the elements of matrix " + matrixName + ":");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = scanner.nextDouble();
            }
        }
        return matrix;
    }

    public static boolean areDimensionsValid(double[][] matrixA, double[][] matrixB) {
        return matrixA.length == matrixB.length && matrixA[0].length == matrixB[0].length;
    }

    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            for (double value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }
}
