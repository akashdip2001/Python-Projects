## Error 01

The error you're encountering, `ModuleNotFoundError: No module named 'kivymd'`, occurs because the `kivymd` module isn't installed in your Python environment. Here’s how to resolve it:

1. **Install KivyMD**: Open your terminal or command prompt and install `kivymd` by running:

   ```bash
   pip install kivymd
   ```

2. **Verify Installation**: After installation, you can check if `kivymd` is correctly installed by entering:

   ```bash
   pip show kivymd
   ```

   This should display details about the `kivymd` package, confirming that it’s installed.

3. **Check Virtual Environment (If Any)**: If you're using a virtual environment, make sure it’s activated when you install the package and run your code.

4. **Run Your Code**: After installation, try running your script again:
   ```bash
   python "c:\Users\akash\Desktop\Py Projects\09 Py to Apk\main.py"
   ```

If you still face issues, ensure that the version of `kivy` you have installed is compatible with `kivymd`, as some older versions might not work well together. You can install compatible versions as follows:

```bash
pip install kivy kivymd
```

<img src="https://github.com/akashdip2001/college-final-year-project/blob/main/img/colour_line.png" >

The installation error you're facing is likely due to dependencies that `kivymd` and `kivy` rely on, particularly the version conflict for `kivy_deps.sdl2_dev`. This can be common on Windows because `kivy` and `kivymd` have some external dependencies. Here are some steps to work around this issue:

### Step 1: Upgrade `pip`, `setuptools`, and `wheel`

First, ensure you have the latest versions of `pip`, `setuptools`, and `wheel` to improve compatibility with newer packages:

```bash
pip install --upgrade pip setuptools wheel
```

### Step 2: Manually Install the Required Dependencies

Since `kivy_deps.sdl2_dev` is causing issues, try manually installing all Kivy dependencies before installing `kivy` and `kivymd`. Run these commands one by one:

```bash
pip install kivy_deps.gstreamer_dev==0.3.3
pip install kivy_deps.sdl2_dev==0.8.0
pip install kivy_deps.glew_dev==0.3.0
pip install kivy_deps.gstreamer==0.1.19
pip install kivy_deps.sdl2==0.1.23
pip install kivy_deps.glew==0.1.12
```

### Step 3: Install `kivy` and `kivymd` Directly

After installing the dependencies, try installing `kivy` and `kivymd`:

```bash
pip install kivy==2.3.0
pip install kivymd==1.2.0
```

### Step 4: Verify Installation

To confirm, check that both `kivy` and `kivymd` are installed correctly:

```bash
pip show kivy
pip show kivymd
```

### Step 5: Run Your Script Again

If the installation completes without issues, try running your script once more:

```bash
python "c:\Users\akash\Desktop\Py Projects\09 Py to Apk\main.py"
```

This approach should resolve the dependency issues by specifying compatible versions explicitly. If there are further errors, let me know so I can assist you with any additional troubleshooting.

<img src="https://github.com/akashdip2001/college-final-year-project/blob/main/img/colour_line.png" >

The errors suggest that certain versions of the `kivy_deps` packages aren’t available for your Python version (likely Python 3.13), which can be causing compatibility issues. Here’s how to work around this:

1. **Check Python Version**: Kivy and KivyMD work best with **Python 3.10 or below**. If you’re using Python 3.13, you may want to try installing Python 3.10, then create a new virtual environment using it. This can avoid many compatibility issues.

2. **Create and Activate a Virtual Environment (Optional but Recommended)**:
   Creating a virtual environment ensures that dependencies do not interfere with your global Python setup. Once you have Python 3.10 installed, create a virtual environment in your project directory:

   ```bash
   python3.10 -m venv kivy_env
   ```

   Activate it:

   - **Windows**: `kivy_env\Scripts\activate`
   - **Mac/Linux**: `source kivy_env/bin/activate`

3. **Install Compatible Kivy and KivyMD Versions**:
   Inside the virtual environment, install the compatible dependencies:

   ```bash
   pip install kivy==2.1.0
   pip install kivymd==1.1.1
   ```

4. **Verify and Run Your Code**:
   After installation, verify the setup:
   ```bash
   pip show kivy
   pip show kivymd
   ```
   Then, try running your script again:
   ```bash
   python "c:\Users\akash\Desktop\Py Projects\09 Py to Apk\main.py"
   ```

This should allow you to proceed without encountering those package version conflicts. Let me know if you face any more issues!

## Error 02

<img src="kivy_python.jpg">
<img src="Screenshot (31).png">

[Google Colab Link](https://colab.research.google.com/drive/1oZQIyIRl7AbND04W6lIT9oWt3PYT-5Rd?usp=sharing)
