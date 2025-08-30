[app]

title = Moundir
package.name = moundir
package.domain = org.novfensec

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = images/*.png

version = 0.1

requirements = python3, kivy==2.3.1, https://github.com/kivymd/KivyMD/archive/master.zip, exceptiongroup, asynckivy, asyncgui, materialyoucolor, android

presplash.filename = %(source.dir)s/images/presplash.png
icon.filename = %(source.dir)s/images/favicon.png

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.1

#
# Android
#

fullscreen = 0
android.api = 33
android.minapi = 21
# android.sdk = 33   ← (❌ احذف هذا السطر)
# android.ndk = 28   ← ما تحتاجه، Buildozer يجيب المناسب تلقائي
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.release_artifact = aab
android.debug_artifact = apk
p4a.branch = develop

#
# iOS
#
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/ios-control/ios-deploy
ios.ios_deploy_branch = master
ios.codesign.allowed = false

[buildozer]
log_level = 2
warn_on_root = 1
