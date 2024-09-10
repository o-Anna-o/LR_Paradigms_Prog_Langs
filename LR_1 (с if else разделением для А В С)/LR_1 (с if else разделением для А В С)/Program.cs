using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LR_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Данная программа предназначена для решения биквадратного уравнения\n");
            // Предполагаем, что коэффициенты A, B, C инициализируются нулевыми значениями
            double A = 0, B = 0, C = 0;

            // Пытаемся получить коэффициенты из параметров командной строки
            if (args.Length == 3)
            {
                //присваивем коэффициентам A, B, C значения из аргументов командной строки
                double.TryParse(args[0], out A);
                double.TryParse(args[1], out B);
                double.TryParse(args[2], out C);

                //если таковые заданы (проверим и если нет - попросим пользователя ввести их вручную)
                if (!double.TryParse(args[0], out A) || !double.TryParse(args[1], out B) || !double.TryParse(args[2], out C))
                {
                    Console.WriteLine("Необходимо ввести вещественное число. Вводите коэффициенты заново.\n");
                }
            }
            else //если аргументы не заданы, их вводит пользователь
            {
                A = ReadDouble("Введите коэффициент A: ");
                B = ReadDouble("Введите коэффициент B: ");
                C = ReadDouble("Введите коэффициент C: ");
            }

            double discriminant = (B * B) - (4 * A * C); //вычислим дискриминант
            Console.WriteLine("Дискриминант = " + discriminant + "\n");

            // Рассмотрим возможные значения дискриминанта
            if (discriminant > 0)
            {
                double TempVal1 = (-B + Math.Sqrt(discriminant)) / (2 * A);
                double TempVal2 = (-B - Math.Sqrt(discriminant)) / (2 * A);

                Console.ForegroundColor = ConsoleColor.Green; 
                if (TempVal1 >= 0)
                {
                    double root1 = Math.Sqrt(TempVal1);
                    double root2 = -Math.Sqrt(TempVal1);

                    Console.WriteLine("Корень 1: {0:F2}", root1);
                    Console.WriteLine("Корень 2: {0:F2}", root2);
                }

                if (TempVal2 >= 0)
                {
                    double root3 = Math.Sqrt(TempVal2);
                    double root4 = -Math.Sqrt(TempVal2);

                    Console.WriteLine("Корень 3: {0:F2}", root3);
                    Console.WriteLine("Корень 4: {0:F2}\n", root4);
                }
                Console.ResetColor();
            }
            else if (discriminant == 0)
            {
                double TempVal = (-B) / (2 * A);
                ProcessSingleRoot(TempVal);
            }
            else
            {
                // Нет корней => выводим сообщение красным цветом
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Корней нет\n");
                Console.ResetColor();
            }
        }

        /// <summary>
        /// Ввод вещественного числа с проверкой корректности ввода
        /// </summary>
        /// <param name="message">Подсказка при вводе</param>
        static double ReadDouble(string message)
        {
            string resultString;
            double resultDouble;
            bool flag;

            do
            {
                Console.Write(message);
                resultString = Console.ReadLine();
                flag = double.TryParse(resultString, out resultDouble);

                if (!flag)
                {
                    Console.WriteLine("Необходимо ввести вещественное число");
                }
            }
            while (!flag);
            return resultDouble;
        }
        static void ProcessSingleRoot(double TempVal)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            if (TempVal >= 0)
            {
                double root1 = Math.Sqrt(TempVal);
                double root2 = -Math.Sqrt(TempVal);

                Console.WriteLine("Корень 1: {0:F2}", root1);
                Console.WriteLine("Корень 2: {0:F2}\n", root2);
            }
            Console.ResetColor();
        }
    }
}
