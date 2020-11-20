# Template Schema (v1)
<dl>
    <dt>engine</dt>
    <dd>The semantic version(s) of the cadCAD engine that this template supports.</dd>
</dl>

<dl>
    <dt>meta</dt>
    <dd>A grouping of various metadata designations.</dd>
</dl>

<dl>
    <dt>meta: name</dt>
    <dd>The name of this template.</dd>
</dl>

<dl>
    <dt>meta: description</dt>
    <dd>A description of this template.</dd>
</dl>

<dl>
    <dt>meta: version</dt>
    <dd>The version of this template (semantic versioning used).</dd>
</dl>

<dl>
    <dt>meta: requirements</dt>
    <dd>The custom requirements.txt file to replace scaffold default.</dd>
</dl>

<dl>
    <dt>scaffold</dt>
    <dd>A grouping of project structure designations.</dd>
</dl>

<dl>
    <dt>scaffold: directories</dt>
    <dd>A list of directory entries. May belong as child to directory entries as well.</dd>
</dl>

<dl>
    <dt>directories: name</dt>
    <dd>Inline content to be added to a created file.</dd>
</dl>

<dl>
    <dt>scaffold: files</dt>
    <dd>A list of file entries. May belong as child to directory entries as well.</dd>
</dl>

<dl>
    <dt>files: name</dt>
    <dd>The name of the file to be created.</dd>
</dl>

<dl>
    <dt>files: source</dt>
    <dd>The file to be copied when creating a file.</dd>
</dl>