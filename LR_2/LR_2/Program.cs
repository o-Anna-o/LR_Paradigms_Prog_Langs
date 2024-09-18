using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;

namespace LR_1
{
    interface IPrint
    {
        void Print();
    }
    abstract class Figure // Класс фигура
    {
        public string Type { get; protected set; } // Тип фигуры (объявление автоопределяемым свойством)
        string _Type;
        public abstract double Area(); // Вычисление площади

        public override string ToString()
        {
            return this.Type + " площадью " + this.Area().ToString("f2");
        }

    }
    class Rectangle : Figure, IPrint
    {
        double height; //высота
        double width; //ширина
        public double Width
        {
            get => this.width;
            set => this.width = value;
        }
        public double Height
        {
            get => this.height;
            set => this.height = value;
        }
        public Rectangle(double h, double w)
        {
            this.height = h;
            this.width = w;
            this.Type = "Прямоугольник";
        }
        public override double Area()
        {
            double result = this.height * this.width;
            return result;
        }
        public void Print()
        {
            Console.WriteLine(this.ToString());
        }
    }
    class Square : Rectangle, IPrint
    {
        public Square(double d) : base(d, d)
        {
            this.Type = "Квадрат";
        }
        public void Print()
        {
            Console.WriteLine(this.ToString());
        }
    }
    class Circle : Figure, IPrint
    {
        double radius;
        public Circle(double r)
        {
            this.radius = r;
            this.Type = "Круг";
        }
        public override double Area()
        {
            double result = Math.PI * this.radius * this.radius;
            return result;
        }
        public void Print()
        {
            Console.WriteLine(this.ToString());
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Rectangle rectangle = new Rectangle(2, 3);
            Square square = new Square(4);
            Circle circle = new Circle(5);

            rectangle.Print();
            square.Print();
            circle.Print();
        }
    }
}


