import VClothing

if __name__ == "__main__":
    print(
    '''
What does this tool do? : 
    > simple tool that makes it easiy to view textures of specific IDs
    > displays the textures and their In-game names for both genders

    
CATEGORIES:

    - accessories  - hair      - legs
    - shoes        - tops      - torso 
    - undershirts  - bracelets - ears
    - glasses      - hats      - watches
    - masks
    '''
    )

    print('\n-------------------------------------------\n')
    popen = str(input("Enter the category to open: "))
    j = VClothing.jsonparse(popen)