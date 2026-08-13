import marimo

__generated_with = "0.23.8"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is a markdown cell where you can add your own name and (optional) your teammate in the following table:

    |Name|SNR|ANR|
    |----|---|----|
    |    |   |    |
    |    |   |    |
    """)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    # add others that you want to use
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python assignment

    The python assignment you can do either on your own or with one other student (i.e. max group size is 2 students).

    The first cell of your notebook, should contain a table with the names and SNRs and ANRs of the group members, like so

    |Name|SNR|ANR|
    |----|---|----|
    |jan boone|12345|u6786|
    |adam smith|56789|u1234|

    See [the webpage](https://janboone.github.io/Python-programming-for-economists/#final_assignment) for details of what we expect to see in this assignment.

    The syntax used in this template is that we describe in code cells as comments what we want you to do in each section and then in a markdow cell give example sentences for the assignment using an adverse selection model.

    To get a better idea of what we are looking for, read the example final assignment with a gender economics model.
    """)
    return


@app.cell
def _():
    ## Topic and research question

    # which paper or economic "phenomenon" do you use for your assignment

    # Briefly explain the part of the paper that you want to explain with the interactive app

    # Formulate the research question: what question do you want to answer using the app? 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Topic and research question (0.5 points)

    In this app we explain the following ... [example for this template: how asymmetric information can prevent the market from functioning efficiently]

    Research question: What is the effect of the consumer type distribution on the efficiency of the market outcome?
    """)
    return


@app.cell
def _():
    ## Motivation 

    # Motivate why this question is interesting.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Motivation (0.5 points)

    If we understand how the type distribution affects efficiency of the market equilibrium, a regulator could affect this value distribution, say through a subsidy scheme
    """)
    return


@app.cell
def _():
    ## Model 

    # Explain the model in the paper using latex to present the equations of the paper. Make sure that the model has the following elements: (i) agents maximizing payoffs, (ii) equilibrium calculation, (iii) one or two parameters that the user of the app can use to learn something related to your research question and (iv) a parameter sweep to understand how sensitive the results are to (some) parameter choices.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Model (1.0 point)

    Consider a market with sellers offering goods which they value at $q \in [a,b]$. Buyers in the market value a good of quality $q$ at $\lambda q$ with the mark-up $\lambda > 1$. Hence it is efficient that all sellers sell their product to a buyer. However, although the seller knows the quality $q$ of their product ...
    """)
    return


@app.cell
def _():
    ## Python code and explanation

    # Give the python code in code cells and use markdown cells to explain why you code things in this way and what the outcomes are of the code cells.

    # The explanation of your code in markdown cells is at least as important as the python code itself.

    # Note that this does require some thought: the python code will not be displayed in app mode but the explanation of the code will be displayed. Hence what you write should make sense both in app and edit view

    # Also the assignment should make sense for people who are only interacting with the app version and cannot see the code cells or will not read this section at all
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python code and explanation (4.0 points)

    The first type distribution that we consider is a uniform distribution on $[a,b]$ where the user can set $a$ and $b$ using sliders...
    """)
    return


@app.cell
def _(mo):
    a_slider = mo.ui.slider(0,10,step=1,value=5,label="low value of uniform distribution $a$")
    return (a_slider,)


@app.cell
def _(a_slider, mo):
    b_slider = mo.ui.slider(a_slider.value,50,step=1,value=10,label="high value of uniform distribution $b$")

    a_slider, b_slider
    return (b_slider,)


@app.cell
def _(a_slider, b_slider, mo):
    mo.md(f"""
    Now we can plot a histogram of 100 draws out of the uniform distribution $[{a_slider.value},{b_slider.value}]$
    """)
    return


@app.cell
def _(a_slider, b_slider, np, plt):
    draws = np.random.uniform(a_slider.value,b_slider.value,size=100)
    plt.hist(draws,bins=20, edgecolor='black')
    plt.title("Histogram of draws from uniform distribution")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can derive the equilibrium in the market as follows...
    """)
    return


@app.cell
def _():
    ## App 

    # make sure that the user understands the parameters that can be interactively chosen
    # why the parameter is important (in light of the research question)
    # what can the user learn from interacting with the app
    # what is the intuition for the result
    # what can be concluded from using the app
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # App (4 points)

    Using the sliders you can see that the market will (partly) collapse if lowerbound $a$ is close to zero. But for $a$ high enough, the market can yield the efficient outcome...

    Using the app we can conclude that ...
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
