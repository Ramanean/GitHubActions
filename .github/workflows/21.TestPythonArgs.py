
name: SimpleWorkflow

on:
  workflow_dispatch
  
jobs:
  job:
    runs-on: ubuntu-latest
    
    steps:
      
      - name: Checkout
        uses: actions/checkout@v4.1.7
        with:      
          repository: ${{ github.repository }}


      - name: Shell Execution
        run: python test1.py "Shan" "Ganesh"
            
