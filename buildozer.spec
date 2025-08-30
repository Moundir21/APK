[app]

# (str) Title of your application
title = Moundir

# (str) Package name
package.name = moundir

# (str) Package domain (needed for android/ios packaging)
package.domain = org.novfensec

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = images/*.png

# (str) Application versioning
version = 0.1

# (str) Requirements
requirements = python3, kivy==2.3.1, https://github.com/kivymd/KivyMD/archive/master.zip, exceptiongroup, asynckivy, asyncgui, materialyoucolor, android

# (str) Presplash image
presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/images/favicon.png

# (str) Orientation (landscape, portrait, portrait-reverse, landscape-reverse)
orientation = portrait

# OSX specific
osx.python_version = 3
osx.kivy_version = 2.3.1

#
# Android specific
#

# Fullscreen or not
fullscreen = 0

# (int) Android API to use (use stable, not latest!)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (int) Android NDK version to use
android.ndk = 28

# Accept SDK licenses automatically
android.accept_sdk_license = True

# Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# Allow backup
android.allow_backup = True

# (str) Artifact formats
android.release_artifact = aab
android.debug_artifact = apk

# python-for-android branch
p4a.branch = develop

#
# iOS specific
#
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/ios-control/ios-deploy
ios.ios_deploy_branch = master
ios.codesign.allowed = false

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
