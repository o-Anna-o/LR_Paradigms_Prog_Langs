(defun factorial (n)
    (if (< n 2) 1
        (* n (factorial (- n 1)) )
    )
)

(defun fibonacci (n)
    (if (< n 2) n
        (+ (fibonacci (- n 1)) (fibonacci (- n 2)) )
    )
)

(defun input (prompt)
    (format t "~a" prompt)
    (read)
)

(defun main ()
    (let ((n (input "Введите число: ")))
        (format t "Факториал числа = ~a" (factorial n) )
        (format t ", а соответствующее число Фибоначчи = ~a" (fibonacci n) )
    )
)

(main)

