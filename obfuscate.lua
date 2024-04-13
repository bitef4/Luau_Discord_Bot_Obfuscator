local Script = [[
--SCRIPT
]]


local function getmodule()
	local mloaded, module = pcall(function()
		return dofile("module.lua")
	end)
	if not mloaded or module == nil then
		if not mloaded then
			print(module)
		end
		print("Put a path correctly! (ex: C:\\path\\to\\module.lua)")
		return getmodule()
	else
		return module
	end
end
local M_ = getmodule()
if not (M_.crypt ~= nil and type(M_.crypt) == 'function') then
	return nil
end
local function getRfile()
	local mpath = "_0xo726422.lua"
	local mloaded, f, err = pcall(function()
		return io.open(mpath, "rb")
	end)
	if not mloaded or f == nil then
		if not mloaded then
			print(f)
		end
		print("Put a path correctly! (ex: savetheoof.lua)")
		return getRfile()
	else
		return f
	end
end

local obrfile = getRfile()
local obrcode = "_0xo726422.lua"
obrfile:close()

local function getWfile()
	local mpath = "_0xo726421.lua"
	local mloaded, f, err = pcall(function()
		return io.open(mpath, "rb")
	end)
	if not mloaded or f == nil then
		if not mloaded then
			print(f)
		end
		print("Put a path correctly! (ex: soof_obfuscated.lua)")
		return getWfile()
	else
		return f
	end
end

local wfile = getWfile()

local _settings = { -- default options
	comment = "// ", -- "--'comment'"
	variablecomment = "lol you have to stop trying to deobfuscate",
	cryptvarcomment = true, -- encrypt variablecomment with bytecode
	variablename = "CRYPTED", -- "local 'variablename' = 'variablecomment' or something"
}

local com_ = "// Obfuscated By obfuscator"
if com_ == "" then
	com_ = _settings.comment
end

local varcom_ = "This Script Were Protected Stop De obfuscating The Script"
if varcom_ == "" then
	varcom_ = _settings.variablecomment
end
--io.write("Variable Name [CRYPTED]> ")
local varnam_ = "CrazyObfuscator"
if varnam_ == "" then
	varnam_ = _settings.variablecomment
end
--io.write("Crypt Var Value [y]/n> ")
local cryvar_ = "y"
local cryyes = true
if cryvar_:lower() == "n" then
	cryyes = false
else
	cryyes = true
end
local options_ = {
	comment = com_, -- "--'comment'"
	variablecomment = varcom_,
	cryptvarcomment = cryyes, -- encrypt variablecomment with bytecode
	variablename = varnam_, -- "local 'variablename' = 'variablecomment' or something"
}
--io.write("Press Enter to continue or ^C to cancel...")io.read()

local memoryleakerlolwhat = M_(Script,options_)

wfile:write(memoryleakerlolwhat)
wfile:close()
print(memoryleakerlolwhat)
--io.write("Done! Press Enter to exit...")io.read()