(defn factorial [n]
    (if (< n 2) 1
        (* n (factorial (dec n)) )
    )
)

(defn fibonacci [n]
    (if (< n 2) n
        (+ (fibonacci (dec n)) (fibonacci (- n 2)) )
    )
)

(defn input [p]
    (println p)
    (read)
)

(defn main[]
    (let [n (input "Введите число: ")]
        (print(str "Факториал числа = " (factorial n)) )
        (println (str ", а соответствующее число Фибоначчи = " (fibonacci n)) )
    )
)

(main)