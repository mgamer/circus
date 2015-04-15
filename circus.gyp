{
'targets': [
{
'target_name': 'Circus',
'type': 'executable',
'mac_bundle': 1,
'include_dirs' : [
'substructure',
],
'sources': [
'src/AppDelegate.swift',
'src/ViewController.swift',
'src/Info.plist',
],
'link_settings': {
'libraries': [

],
},
'xcode_settings' : {
'INFOPLIST_FILE' : 'src/Info.plist',
'SDKROOT': 'iphoneos',
'TARGETED_DEVICE_FAMILY': '1,2',
	'CODE_SIGN_IDENTITY': 'iPhone Developer',
'IPHONEOS_DEPLOYMENT_TARGET': '8.3',
'ARCHS': '$(ARCHS_UNIVERSAL_IPHONE_OS)',
'HEADER_SEARCH_PATHS': '$(inherited)',
'CLANG_ENABLE_OBJC_ARC': 'YES',
},
},
]
}
