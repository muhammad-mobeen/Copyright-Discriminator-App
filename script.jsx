function main() {

  var num = 1;

  //Get Current Open Document Object.

  var doc = app.activeDocument;

  for (var i = 1; i < doc.layers.length; i++) {

    //Active Layer

    doc.activeLayer = doc.layers[i];

    // Visible Each Layer one by one

    doc.layers[i].visible = true;

    // Method To Resize Layer according to width and Height

    var theBounds = doc.activeLayer.bounds;

    var layerWidth = theBounds[2] - theBounds[0];

    var layerHeight = theBounds[3] - theBounds[1];

    var layer_center_x = theBounds[0] + layerWidth / 2;

    var layer_center_y = theBounds[1] + layerHeight / 2;

    var doc_center_x = doc.width / 2;

    var doc_center_y = doc.height / 2;

    var shift_x = doc_center_x - layer_center_x;

    var shift_y = doc_center_y - layer_center_y;

    doc.activeLayer.translate(shift_x, shift_y);

    var scale_w = doc.width / layerWidth;

    var scale_h = doc.height / layerHeight;

    var scale = Math.max(scale_w, scale_h) * 100;

    // prompt("Width",scale);

    doc.activeLayer.resize(scale + 30, scale + 30, AnchorPosition.MIDDLECENTER);

    //Satutation Method Call

    // hueSaturation(60, -50, 0);

    // Rotate Active Layer

    doc.activeLayer.rotate(6, AnchorPosition.MIDDLECENTER);

    //Flip Method Call

    // use 'Hrzn' for horizontal flip

    //use  'Vrtc' for  Vertical flip

    flipimage('Hrzn');

    num++;

    Save(num);

    Revert();

    doc.layers[i].visible = false;
  }

  function hueSaturation(hue, saturation, lightness) {

    var s2t = function (s) {

      return app.stringIDToTypeID(s);

    };

    var descriptor = new ActionDescriptor();

    var descriptor2 = new ActionDescriptor();

    var list = new ActionList();

    descriptor.putEnumerated(s2t("presetKind"), s2t("presetKindType"), s2t("presetKindCustom"));

    descriptor.putBoolean(s2t("colorize"), false);

    descriptor2.putInteger(s2t("hue"), hue);

    descriptor2.putInteger(s2t("saturation"), saturation);

    descriptor2.putInteger(s2t("lightness"), lightness);

    list.putObject(s2t("hueSatAdjustmentV2"), descriptor2);

    descriptor.putList(s2t("adjustment"), list);

    executeAction(s2t("hueSaturation"), descriptor, DialogModes.NO);

  }
  function flipimage(pos) {

    var descriptor = new ActionDescriptor();

    descriptor.putEnumerated(charIDToTypeID('Axis'), charIDToTypeID('Ornt'), charIDToTypeID(pos));

    executeAction(charIDToTypeID('Flip'), descriptor, DialogModes.NO);

  }

  function Save(num) {

    var outFolder = app.activeDocument; // psd name

    var outPath = outFolder.path;

    var fName = "Photoshoped_images"; // define folder name

    var f = new Folder(outPath + "/" + fName);

    if (!f.exists) {

      f.create();

    }
    var saveFile = new File(outPath + "/" + fName + "/" + "Pattern_" + num + ".png");

    pngSaveOptions = new PNGSaveOptions();

    pngSaveOptions.interlaced = false;

    app.activeDocument.saveAs(
      saveFile,
      pngSaveOptions,
      true,
      Extension.LOWERCASE
    );

  }

  function Revert() {

    var idRvrt = charIDToTypeID("Rvrt");

    executeAction(idRvrt, undefined, DialogModes.NO);

  }

}

app.activeDocument.suspendHistory("Hue/Saturation All Layers", "main()");