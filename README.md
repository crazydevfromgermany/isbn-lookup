---

# Buecher API Class

The `BuecherGrabber` class is a Python class designed to simplify the process of extracting information from the [buecher.de](https://www.buecher.de) website using ISBN. It encapsulates functionality for retrieving details about a book based on its ISBN, including product details, descriptions, and more.

## Usage

To use the `BuecherGrabber` class, follow these steps:

1. **Initialization:**
    ```python
    # Replace 'your_isbn_here' with the actual ISBN
    grabber_instance = BuecherGrabber('your_isbn_here')
    ```

2. **Grab Information:**
    ```python
    grabber_instance.grab_info()
    ```

3. **Print Information:**
    ```python
    grabber_instance.print_info()
    ```

4. **Accessing Specific Details:**
    
  
  ## Accessing Specific Details
  
  The `BuecherGrabber` class allows direct access to specific details through attributes. Below are examples of accessing common details:
  
  ### `beschreibung`
  
  ```python
  # Accessing the book description
  print(grabber_instance.beschreibung)
  ```
  
  ### `inhaltsverzeichnis`
  
  ```python
  # Accessing the table of contents
  print(grabber_instance.inhaltsverzeichnis)
  ```
  
  ### `preis`
  
  ```python
  # Accessing the book price
  print(grabber_instance.preis)
  ```
  
  ### `author`
  
  ```python
  # Accessing the book author
  print(grabber_instance.author)
  ```
  
  ### `verlag`
  
  ```python
  # Accessing the book publisher
  print(grabber_instance.verlag)
  ```
  
  ### `seitenzahl`
  
  ```python
  # Accessing the number of pages
  print(grabber_instance.seitenzahl)
  ```
  
  ### `erscheinungstermin`
  
  ```python
  # Accessing the book release date
  print(grabber_instance.erscheinungstermin)
  ```
  
  ### `sprache`
  
  ```python
  # Accessing the book language
  print(grabber_instance.sprache)
  ```
  
  ### `isbn_13`
  
  ```python
  # Accessing the ISBN-13
  print(grabber_instance.isbn_13)
  ```
  
  ### `artikelnr`
  
  ```python
  # Accessing the article number
  print(grabber_instance.artikelnr)
  ```

## Class Methods

### `grab_info()`

The `grab_info` method initiates the process of fetching information from the buecher.de website based on the provided ISBN. It retrieves details such as product descriptions, product details, and the table of contents.

### `print_info()`

The `print_info` method displays the extracted information, including product details, description, and the article URL.

### `checker()`

The `checker` method checks the availability of the book on the buecher.de website and updates the class attributes accordingly.

## Class Attributes

### `isbn`

- Type: String
- Description: The ISBN of the book used to initialize the class instance.

### `book_details`

- Type: Dictionary
- Description: A dictionary containing details about the book, including product details, description, and table of contents.

### `artikel_url`

- Type: String
- Description: The URL of the article on buecher.de associated with the provided ISBN.

### `html`

- Type: String
- Description: The HTML content fetched from buecher.de based on the provided ISBN.

## Example

```python
# Replace 'your_isbn_here' with the actual ISBN
grabber_instance = BuecherGrabber('your_isbn_here')
grabber_instance.grab_info()
grabber_instance.print_info()
print(grabber_instance.beschreibung)
print(grabber_instance.inhaltsverzeichnis)
```

This class simplifies the process of retrieving book details from buecher.de and provides convenient access to specific details as attributes.

---

