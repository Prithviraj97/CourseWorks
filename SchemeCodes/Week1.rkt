#lang scheme

;;CSCI 416 Project1
;;Week 1
;;Author: Prithvi Raj Singh

;;(C.1) Creating a structure using the define-struct function with description of grocery items at store,
;;      including the price, id, description of items
(define-struct product (id description price))

;;(d) Defining list of struct object with their own id, description, and price
(define grocerylist (list (make-product 1 "Potato" 6.39) (make-product 2 "Apple" 3.19)
                         (make-product 3 "Tomato" 3.79) (make-product 4 "Orange" 1.99)
                         (make-product 5 "Milk" 3.99) (make-product 6 "Yogurt" 4.49)
                         (make-product 7 "Cereals" 2.99) (make-product 8 "Pears" 4.79)
                         (make-product 9 "PeanutButter" 4.29) (make-product 10 "Banana" 2.39)))
;; (e.i) The lookup function that takes id and a list as parameter and returns the
;;       object from the list that matches the id.
(define (lookup id list) (cond ( (null? list) '())
                               ( (= id (product-id (car list))) (car list))
                               (else (lookup id (cdr list))) )) ;;take parameters, make sure the list is null, return id and object
(lookup 1 grocerylist)

;;(e.ii) The getdesc takes id as a parameter and uses lookup function to find the object with description.
(define (getdesc id)
  (let ( [list (lookup id grocerylist)])
    (if (product? list) (  product-description list) #f)))

(getdesc 5) ;;testing the getdesc function

;;(e.iii) The getprice function takes id as a parameter and uses lookup function to get the price and detail of item.
(define (getprice id)
  (let ( [list1 (lookup id grocerylist)])
    (if (product? list1) (product-price list1) #f)))

(getprice 7)

;;(e.iv) The subtotal takes list of id's as a parameter and use format function to display subtotal
(define (subtotal id-list)
  (if (null? id-list)
      0
      (+ (getprice (car id-list)) (subtotal (cdr id-list))) ))
(subtotal '(2 4 6 8))

;;(e.v) The total function will take id as a paramter and uses the subtotal plus 11% tax to calculate total
(define (total id-list)
  (let* ( (subtotal (subtotal id-list))
          ( total (+ subtotal (* subtotal .11))))
          (format "Total: ~s" total)))
(total '(2 4 6 8)) ;;test code 

;;(e.vi) The getlist fucntion will return the list with id, description and the helper function will take
;;       list as a paramter and makes a masterlist
(define (getlist)
  (helper grocerylist))

(define (helper lst1)
  (if (null? lst1)
      '()
      (let* ( (id (product-id (car lst1)))
        (return-list (list id (getdesc id) (getprice id))))
  (cons return-list (helper (cdr lst1))) )))

(getlist)

  

