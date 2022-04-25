
<!--## Adaptable config file -->

From the documentation:

> One important variable that is passed to almost all the workflows invoked in Main.xaml is the Config dictionary. This variable is initialized by the InitAllSettings.xaml workflow in the Initialization state, and it contains all the configuration declared in the Config.xlsx file. Since it is a dictionary, the values in Config can be accessed by its keys, like Config(“Department”) or Config(“System1_URL”)
>
> For easier manipulation, this configuration file is an Excel workbook with three sheets:
> - Settings: Configuration values to be used throughout the project and that usually depend on the environment being used. For example, names of queues, folder paths or URLs for web systems.
> - Constants: Values that are supposed to be the same across all deployments of the workflow. For example, the department name or the bank name to be used as input in a certain screen.
> - Assets: Values defined as assets in Orchest
>
> @see: Documentation\REFramework Documentation-EN.pdf

##{{include.headingmodifier}} Standard:

1. Main.xaml > Initialization (State)
1. If first run, read local configuration file (If)
1. Invoke InitAllSettings workflow (InvokeWorkflowFile)
  - { in_ConfigFile; value = Data\Config.xlsx, Type = String, Direction = In }

The standard REFramework reads in Main.xaml during the first run of the Initialization state by invoking the InitAllSettings workflow the Excel file as located by the input argument in_ConfigFile, defaulting to Data\Config.xlsx. The location of this config file cannot be declared otherwise.

##{{include.headingmodifier}} Customization:

1. md Framework
1. md Data
1. `Copy-Item ..\RoboticEnterpriseFramework\Framework\InitAllSettings.xaml Framework\`
1. `Copy-Item ..\RoboticEnterpriseFramework\Data\Config.xlsx .\Data\`
1. `Copy-Item ..\RoboticEnterpriseFramework\Data\Config.xlsx .\Data\Config_dev.xlsx`
1. In Main.xaml, create an input string argument `in_ConfigFile` defaulting to  Data\Config_dev.xlsx
1. In the InitAllSettings.xaml workflow file, remove the default value for in_ConfigFile
1. In Main.xaml > Initialization (State) when invoking `Framework\InitAllSettings.xaml` change in the collection of the invoked workflow's argument the value for `in_ConfigFile` to `in_ConfigFile`.

That way you can supply in UiPath Orchestrator a parameter for either Process or Job with a different location. This customization even allows for multiple Processes of the same Package with differing default config files. 


###{{include.headingmodifier}} Excursion: Use REFramework's Config dictionary in non-REFramework projects

To make any UiPath RPA project portable and increase its maintainability a re-use of REFramework's config file feature is trivial to achieve. The following steps will make the Config dictionary available in any other project.

1. From a REFramework project*, copy over the files `Framework\InitAllSettings.xaml` and `Data\Config.xlsx` to equally named folders in the local project.
```Powershell
md Framework
md Data
Copy-Item ..\RoboticEnterpriseFramework\Framework\InitAllSettings.xaml Framework\
Copy-Item ..\RoboticEnterpriseFramework\Data\Config.xlsx .\Data\
Copy-Item ..\RoboticEnterpriseFramework\Data\Config.xlsx .\Data\Config_dev.xlsx
```
1. Duplicate `Data\Config.xlsx` to e.g. `Data\Config_dev.xlsx`
1. In Main.xaml, create an input string argument `in_ConfigFile` defaulting to  Data\Config_dev.xlsx
1. In the InitAllSettings.xaml workflow file, remove the default value for in_ConfigFile
1. In Main.xaml, uns an `Invoke Workflow File` activity with the `Workflow File Name` set to "Framework/InitAllSettings.xaml" and set the argument in_ConfigFile to the value in_ConfigFile (sic).

This makes Config available to pass as an argument into any invoked workflow file.

*) The REFramework is only a few clicks away in UiPath Studio via Home > Templates.
