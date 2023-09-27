import subprocess


def deploy_resources():

    subprocess.run(["az", "bicep", "build", "--file",
                   "bicep-templates/main.bicep"])

    subprocess.run(["az", "deployment", "sub", "create",
                   "--location", "westeurope", "--template-file", "bicep-templates/main.json"])


def delete_resource_group():

    print("⏳Deleting the resource group...")
    result = subprocess.run(["az", "group", "delete", "--name",
                            "onBoardingResourceGroup", "--yes"], capture_output=True, text=True)

    if result.returncode == 0:
        print("✅Resource group deleted successfully!")
    else:
        print(f"🚫Failed to delete resource group. Error: {result.stderr}")
