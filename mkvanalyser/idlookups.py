id_table = {
  # EBML general
  0xEC: {'name': 'Void', 'type': 'binary'},
  0xBF: {'name': 'CRC-32', 'type': 'binary'},
  0x1A45DFA3: {'name': 'EBML', 'type': 'master'},
  0x4286: {'name': 'EBMLVersion', 'type': 'uinteger'},
  0x42F7: {'name': 'EBMLReadVersion', 'type': 'uinteger'},
  0x42F2: {'name': 'EBMLMaxIDLength', 'type': 'uinteger'},
  0x42F3: {'name': 'EBMLMaxSizeLength', 'type': 'uinteger'},
  0x4282: {'name': 'DocType', 'type': 'string'},
  0x4287: {'name': 'DocTypeVersion', 'type': 'uinteger'},
  0x4285: {'name': 'DocTypeReadVersion', 'type': 'uinteger'},
  0x1B538667: {'name': 'SignatureSlot', 'type': 'master'},
  0x7E8A: {'name': 'SignatureAlgo', 'type': 'uinteger'},
  0x7E9A: {'name': 'SignatureHash', 'type': 'uinteger'},
  0x7EA5: {'name': 'SignaturePublicKey', 'type': 'binary'},
  0x7EB5: {'name': 'Signature', 'type': 'binary'},
  0x7E5B: {'name': 'SignatureElements', 'type': 'master'},
  0x7E7B: {'name': 'SignatureElementList', 'type': 'master'},
  0x6532: {'name': 'SignedElement', 'type': 'binary'},
  # Matroska specific
  0x42F2: {'name': 'EBMLMaxIDLength', 'type': 'uinteger'},
  0x42F3: {'name': 'EBMLMaxSizeLength', 'type': 'uinteger'},
  0x18538067: {'name': 'Segment', 'type': 'master'},
  0x114D9B74: {'name': 'SeekHead', 'type': 'master'},
  0x4DBB: {'name': 'Seek', 'type': 'master'},
  0x53AB: {'name': 'SeekID', 'type': 'binary'},
  0x53AC: {'name': 'SeekPosition', 'type': 'uinteger'},
  0x1549A966: {'name': 'Info', 'type': 'master'},
  0x73A4: {'name': 'SegmentUID', 'type': 'binary'},
  0x7384: {'name': 'SegmentFilename', 'type': 'utf-8'},
  0x3CB923: {'name': 'PrevUID', 'type': 'binary'},
  0x3C83AB: {'name': 'PrevFilename', 'type': 'utf-8'},
  0x3EB923: {'name': 'NextUID', 'type': 'binary'},
  0x3E83BB: {'name': 'NextFilename', 'type': 'utf-8'},
  0x4444: {'name': 'SegmentFamily', 'type': 'binary'},
  0x6924: {'name': 'ChapterTranslate', 'type': 'master'},
  0x69A5: {'name': 'ChapterTranslateID', 'type': 'binary'},
  0x69BF: {'name': 'ChapterTranslateCodec', 'type': 'uinteger'},
  0x69FC: {'name': 'ChapterTranslateEditionUID', 'type': 'uinteger'},
  0x2AD7B1: {'name': 'TimestampScale', 'type': 'uinteger'},
  0x4489: {'name': 'Duration', 'type': 'float'},
  0x4461: {'name': 'DateUTC', 'type': 'date'},
  0x7BA9: {'name': 'Title', 'type': 'utf-8'},
  0x4D80: {'name': 'MuxingApp', 'type': 'utf-8'},
  0x5741: {'name': 'WritingApp', 'type': 'utf-8'},
  0x1F43B675: {'name': 'Cluster', 'type': 'master'},
  0xE7: {'name': 'Timestamp', 'type': 'uinteger'},
  0x5854: {'name': 'SilentTracks', 'type': 'master'},
  0x58D7: {'name': 'SilentTrackNumber', 'type': 'uinteger'},
  0xA7: {'name': 'Position', 'type': 'uinteger'},
  0xAB: {'name': 'PrevSize', 'type': 'uinteger'},
  0xA3: {'name': 'SimpleBlock', 'type': 'binary'},
  0xA0: {'name': 'BlockGroup', 'type': 'master'},
  0xA1: {'name': 'Block', 'type': 'binary'},
  0xA2: {'name': 'BlockVirtual', 'type': 'binary'},
  0x75A1: {'name': 'BlockAdditions', 'type': 'master'},
  0xA6: {'name': 'BlockMore', 'type': 'master'},
  0xEE: {'name': 'BlockAddID', 'type': 'uinteger'},
  0xA5: {'name': 'BlockAdditional', 'type': 'binary'},
  0x9B: {'name': 'BlockDuration', 'type': 'uinteger'},
  0xFA: {'name': 'ReferencePriority', 'type': 'uinteger'},
  0xFB: {'name': 'ReferenceBlock', 'type': 'integer'},
  0xFD: {'name': 'ReferenceVirtual', 'type': 'integer'},
  0xA4: {'name': 'CodecState', 'type': 'binary'},
  0x75A2: {'name': 'DiscardPadding', 'type': 'integer'},
  0x8E: {'name': 'Slices', 'type': 'master'},
  0xE8: {'name': 'TimeSlice', 'type': 'master'},
  0xCC: {'name': 'LaceNumber', 'type': 'uinteger'},
  0xCD: {'name': 'FrameNumber', 'type': 'uinteger'},
  0xCB: {'name': 'BlockAdditionID', 'type': 'uinteger'},
  0xCE: {'name': 'Delay', 'type': 'uinteger'},
  0xCF: {'name': 'SliceDuration', 'type': 'uinteger'},
  0xC8: {'name': 'ReferenceFrame', 'type': 'master'},
  0xC9: {'name': 'ReferenceOffset', 'type': 'uinteger'},
  0xCA: {'name': 'ReferenceTimestamp', 'type': 'uinteger'},
  0xAF: {'name': 'EncryptedBlock', 'type': 'binary'},
  0x1654AE6B: {'name': 'Tracks', 'type': 'master'},
  0xAE: {'name': 'TrackEntry', 'type': 'master'},
  0xD7: {'name': 'TrackNumber', 'type': 'uinteger'},
  0x73C5: {'name': 'TrackUID', 'type': 'uinteger'},
  0x83: {'name': 'TrackType', 'type': 'uinteger'},
  0xB9: {'name': 'FlagEnabled', 'type': 'uinteger'},
  0x88: {'name': 'FlagDefault', 'type': 'uinteger'},
  0x55AA: {'name': 'FlagForced', 'type': 'uinteger'},
  0x55AB: {'name': 'FlagHearingImpaired', 'type': 'uinteger'},
  0x55AC: {'name': 'FlagVisualImpaired', 'type': 'uinteger'},
  0x55AD: {'name': 'FlagTextDescriptions', 'type': 'uinteger'},
  0x55AE: {'name': 'FlagOriginal', 'type': 'uinteger'},
  0x55AF: {'name': 'FlagCommentary', 'type': 'uinteger'},
  0x9C: {'name': 'FlagLacing', 'type': 'uinteger'},
  0x6DE7: {'name': 'MinCache', 'type': 'uinteger'},
  0x6DF8: {'name': 'MaxCache', 'type': 'uinteger'},
  0x23E383: {'name': 'DefaultDuration', 'type': 'uinteger'},
  0x234E7A: {'name': 'DefaultDecodedFieldDuration', 'type': 'uinteger'},
  0x23314F: {'name': 'TrackTimestampScale', 'type': 'float'},
  0x537F: {'name': 'TrackOffset', 'type': 'integer'},
  0x55EE: {'name': 'MaxBlockAdditionID', 'type': 'uinteger'},
  0x41E4: {'name': 'BlockAdditionMapping', 'type': 'master'},
  0x41F0: {'name': 'BlockAddIDValue', 'type': 'uinteger'},
  0x41A4: {'name': 'BlockAddIDName', 'type': 'string'},
  0x41E7: {'name': 'BlockAddIDType', 'type': 'uinteger'},
  0x41ED: {'name': 'BlockAddIDExtraData', 'type': 'binary'},
  0x536E: {'name': 'Name', 'type': 'utf-8'},
  0x22B59C: {'name': 'Language', 'type': 'string'},
  0x22B59D: {'name': 'LanguageIETF', 'type': 'string'},
  0x86: {'name': 'CodecID', 'type': 'string'},
  0x63A2: {'name': 'CodecPrivate', 'type': 'binary'},
  0x258688: {'name': 'CodecName', 'type': 'utf-8'},
  0x7446: {'name': 'AttachmentLink', 'type': 'uinteger'},
  0x3A9697: {'name': 'CodecSettings', 'type': 'utf-8'},
  0x3B4040: {'name': 'CodecInfoURL', 'type': 'string'},
  0x26B240: {'name': 'CodecDownloadURL', 'type': 'string'},
  0xAA: {'name': 'CodecDecodeAll', 'type': 'uinteger'},
  0x6FAB: {'name': 'TrackOverlay', 'type': 'uinteger'},
  0x56AA: {'name': 'CodecDelay', 'type': 'uinteger'},
  0x56BB: {'name': 'SeekPreRoll', 'type': 'uinteger'},
  0x6624: {'name': 'TrackTranslate', 'type': 'master'},
  0x66A5: {'name': 'TrackTranslateTrackID', 'type': 'binary'},
  0x66BF: {'name': 'TrackTranslateCodec', 'type': 'uinteger'},
  0x66FC: {'name': 'TrackTranslateEditionUID', 'type': 'uinteger'},
  0xE0: {'name': 'Video', 'type': 'master'},
  0x9A: {'name': 'FlagInterlaced', 'type': 'uinteger'},
  0x9D: {'name': 'FieldOrder', 'type': 'uinteger'},
  0x53B8: {'name': 'StereoMode', 'type': 'uinteger'},
  0x53C0: {'name': 'AlphaMode', 'type': 'uinteger'},
  0x53B9: {'name': 'OldStereoMode', 'type': 'uinteger'},
  0xB0: {'name': 'PixelWidth', 'type': 'uinteger'},
  0xBA: {'name': 'PixelHeight', 'type': 'uinteger'},
  0x54AA: {'name': 'PixelCropBottom', 'type': 'uinteger'},
  0x54BB: {'name': 'PixelCropTop', 'type': 'uinteger'},
  0x54CC: {'name': 'PixelCropLeft', 'type': 'uinteger'},
  0x54DD: {'name': 'PixelCropRight', 'type': 'uinteger'},
  0x54B0: {'name': 'DisplayWidth', 'type': 'uinteger'},
  0x54BA: {'name': 'DisplayHeight', 'type': 'uinteger'},
  0x54B2: {'name': 'DisplayUnit', 'type': 'uinteger'},
  0x54B3: {'name': 'AspectRatioType', 'type': 'uinteger'},
  0x2EB524: {'name': 'UncompressedFourCC', 'type': 'binary'},
  0x2FB523: {'name': 'GammaValue', 'type': 'float'},
  0x2383E3: {'name': 'FrameRate', 'type': 'float'},
  0x55B0: {'name': 'Colour', 'type': 'master'},
  0x55B1: {'name': 'MatrixCoefficients', 'type': 'uinteger'},
  0x55B2: {'name': 'BitsPerChannel', 'type': 'uinteger'},
  0x55B3: {'name': 'ChromaSubsamplingHorz', 'type': 'uinteger'},
  0x55B4: {'name': 'ChromaSubsamplingVert', 'type': 'uinteger'},
  0x55B5: {'name': 'CbSubsamplingHorz', 'type': 'uinteger'},
  0x55B6: {'name': 'CbSubsamplingVert', 'type': 'uinteger'},
  0x55B7: {'name': 'ChromaSitingHorz', 'type': 'uinteger'},
  0x55B8: {'name': 'ChromaSitingVert', 'type': 'uinteger'},
  0x55B9: {'name': 'Range', 'type': 'uinteger'},
  0x55BA: {'name': 'TransferCharacteristics', 'type': 'uinteger'},
  0x55BB: {'name': 'Primaries', 'type': 'uinteger'},
  0x55BC: {'name': 'MaxCLL', 'type': 'uinteger'},
  0x55BD: {'name': 'MaxFALL', 'type': 'uinteger'},
  0x55D0: {'name': 'MasteringMetadata', 'type': 'master'},
  0x55D1: {'name': 'PrimaryRChromaticityX', 'type': 'float'},
  0x55D2: {'name': 'PrimaryRChromaticityY', 'type': 'float'},
  0x55D3: {'name': 'PrimaryGChromaticityX', 'type': 'float'},
  0x55D4: {'name': 'PrimaryGChromaticityY', 'type': 'float'},
  0x55D5: {'name': 'PrimaryBChromaticityX', 'type': 'float'},
  0x55D6: {'name': 'PrimaryBChromaticityY', 'type': 'float'},
  0x55D7: {'name': 'WhitePointChromaticityX', 'type': 'float'},
  0x55D8: {'name': 'WhitePointChromaticityY', 'type': 'float'},
  0x55D9: {'name': 'LuminanceMax', 'type': 'float'},
  0x55DA: {'name': 'LuminanceMin', 'type': 'float'},
  0x7670: {'name': 'Projection', 'type': 'master'},
  0x7671: {'name': 'ProjectionType', 'type': 'uinteger'},
  0x7672: {'name': 'ProjectionPrivate', 'type': 'binary'},
  0x7673: {'name': 'ProjectionPoseYaw', 'type': 'float'},
  0x7674: {'name': 'ProjectionPosePitch', 'type': 'float'},
  0x7675: {'name': 'ProjectionPoseRoll', 'type': 'float'},
  0xE1: {'name': 'Audio', 'type': 'master'},
  0xB5: {'name': 'SamplingFrequency', 'type': 'float'},
  0x78B5: {'name': 'OutputSamplingFrequency', 'type': 'float'},
  0x9F: {'name': 'Channels', 'type': 'uinteger'},
  0x7D7B: {'name': 'ChannelPositions', 'type': 'binary'},
  0x6264: {'name': 'BitDepth', 'type': 'uinteger'},
  0xE2: {'name': 'TrackOperation', 'type': 'master'},
  0xE3: {'name': 'TrackCombinePlanes', 'type': 'master'},
  0xE4: {'name': 'TrackPlane', 'type': 'master'},
  0xE5: {'name': 'TrackPlaneUID', 'type': 'uinteger'},
  0xE6: {'name': 'TrackPlaneType', 'type': 'uinteger'},
  0xE9: {'name': 'TrackJoinBlocks', 'type': 'master'},
  0xED: {'name': 'TrackJoinUID', 'type': 'uinteger'},
  0xC0: {'name': 'TrickTrackUID', 'type': 'uinteger'},
  0xC1: {'name': 'TrickTrackSegmentUID', 'type': 'binary'},
  0xC6: {'name': 'TrickTrackFlag', 'type': 'uinteger'},
  0xC7: {'name': 'TrickMasterTrackUID', 'type': 'uinteger'},
  0xC4: {'name': 'TrickMasterTrackSegmentUID', 'type': 'binary'},
  0x6D80: {'name': 'ContentEncodings', 'type': 'master'},
  0x6240: {'name': 'ContentEncoding', 'type': 'master'},
  0x5031: {'name': 'ContentEncodingOrder', 'type': 'uinteger'},
  0x5032: {'name': 'ContentEncodingScope', 'type': 'uinteger'},
  0x5033: {'name': 'ContentEncodingType', 'type': 'uinteger'},
  0x5034: {'name': 'ContentCompression', 'type': 'master'},
  0x4254: {'name': 'ContentCompAlgo', 'type': 'uinteger'},
  0x4255: {'name': 'ContentCompSettings', 'type': 'binary'},
  0x5035: {'name': 'ContentEncryption', 'type': 'master'},
  0x47E1: {'name': 'ContentEncAlgo', 'type': 'uinteger'},
  0x47E2: {'name': 'ContentEncKeyID', 'type': 'binary'},
  0x47E7: {'name': 'ContentEncAESSettings', 'type': 'master'},
  0x47E8: {'name': 'AESSettingsCipherMode', 'type': 'uinteger'},
  0x47E3: {'name': 'ContentSignature', 'type': 'binary'},
  0x47E4: {'name': 'ContentSigKeyID', 'type': 'binary'},
  0x47E5: {'name': 'ContentSigAlgo', 'type': 'uinteger'},
  0x47E6: {'name': 'ContentSigHashAlgo', 'type': 'uinteger'},
  0x1C53BB6B: {'name': 'Cues', 'type': 'master'},
  0xBB: {'name': 'CuePoint', 'type': 'master'},
  0xB3: {'name': 'CueTime', 'type': 'uinteger'},
  0xB7: {'name': 'CueTrackPositions', 'type': 'master'},
  0xF7: {'name': 'CueTrack', 'type': 'uinteger'},
  0xF1: {'name': 'CueClusterPosition', 'type': 'uinteger'},
  0xF0: {'name': 'CueRelativePosition', 'type': 'uinteger'},
  0xB2: {'name': 'CueDuration', 'type': 'uinteger'},
  0x5378: {'name': 'CueBlockNumber', 'type': 'uinteger'},
  0xEA: {'name': 'CueCodecState', 'type': 'uinteger'},
  0xDB: {'name': 'CueReference', 'type': 'master'},
  0x96: {'name': 'CueRefTime', 'type': 'uinteger'},
  0x97: {'name': 'CueRefCluster', 'type': 'uinteger'},
  0x535F: {'name': 'CueRefNumber', 'type': 'uinteger'},
  0xEB: {'name': 'CueRefCodecState', 'type': 'uinteger'},
  0x1941A469: {'name': 'Attachments', 'type': 'master'},
  0x61A7: {'name': 'AttachedFile', 'type': 'master'},
  0x467E: {'name': 'FileDescription', 'type': 'utf-8'},
  0x466E: {'name': 'FileName', 'type': 'utf-8'},
  0x4660: {'name': 'FileMimeType', 'type': 'string'},
  0x465C: {'name': 'FileData', 'type': 'binary'},
  0x46AE: {'name': 'FileUID', 'type': 'uinteger'},
  0x4675: {'name': 'FileReferral', 'type': 'binary'},
  0x4661: {'name': 'FileUsedStartTime', 'type': 'uinteger'},
  0x4662: {'name': 'FileUsedEndTime', 'type': 'uinteger'},
  0x1043A770: {'name': 'Chapters', 'type': 'master'},
  0x45B9: {'name': 'EditionEntry', 'type': 'master'},
  0x45BC: {'name': 'EditionUID', 'type': 'uinteger'},
  0x45BD: {'name': 'EditionFlagHidden', 'type': 'uinteger'},
  0x45DB: {'name': 'EditionFlagDefault', 'type': 'uinteger'},
  0x45DD: {'name': 'EditionFlagOrdered', 'type': 'uinteger'},
  0xB6: {'name': 'ChapterAtom', 'type': 'master'},
  0x73C4: {'name': 'ChapterUID', 'type': 'uinteger'},
  0x5654: {'name': 'ChapterStringUID', 'type': 'utf-8'},
  0x91: {'name': 'ChapterTimeStart', 'type': 'uinteger'},
  0x92: {'name': 'ChapterTimeEnd', 'type': 'uinteger'},
  0x98: {'name': 'ChapterFlagHidden', 'type': 'uinteger'},
  0x4598: {'name': 'ChapterFlagEnabled', 'type': 'uinteger'},
  0x6E67: {'name': 'ChapterSegmentUID', 'type': 'binary'},
  0x6EBC: {'name': 'ChapterSegmentEditionUID', 'type': 'uinteger'},
  0x63C3: {'name': 'ChapterPhysicalEquiv', 'type': 'uinteger'},
  0x8F: {'name': 'ChapterTrack', 'type': 'master'},
  0x89: {'name': 'ChapterTrackUID', 'type': 'uinteger'},
  0x80: {'name': 'ChapterDisplay', 'type': 'master'},
  0x85: {'name': 'ChapString', 'type': 'utf-8'},
  0x437C: {'name': 'ChapLanguage', 'type': 'string'},
  0x437D: {'name': 'ChapLanguageIETF', 'type': 'string'},
  0x437E: {'name': 'ChapCountry', 'type': 'string'},
  0x6944: {'name': 'ChapProcess', 'type': 'master'},
  0x6955: {'name': 'ChapProcessCodecID', 'type': 'uinteger'},
  0x450D: {'name': 'ChapProcessPrivate', 'type': 'binary'},
  0x6911: {'name': 'ChapProcessCommand', 'type': 'master'},
  0x6922: {'name': 'ChapProcessTime', 'type': 'uinteger'},
  0x6933: {'name': 'ChapProcessData', 'type': 'binary'},
  0x1254C367: {'name': 'Tags', 'type': 'master'},
  0x7373: {'name': 'Tag', 'type': 'master'},
  0x63C0: {'name': 'Targets', 'type': 'master'},
  0x68CA: {'name': 'TargetTypeValue', 'type': 'uinteger'},
  0x63CA: {'name': 'TargetType', 'type': 'string'},
  0x63C5: {'name': 'TagTrackUID', 'type': 'uinteger'},
  0x63C9: {'name': 'TagEditionUID', 'type': 'uinteger'},
  0x63C4: {'name': 'TagChapterUID', 'type': 'uinteger'},
  0x63C6: {'name': 'TagAttachmentUID', 'type': 'uinteger'},
  0x67C8: {'name': 'SimpleTag', 'type': 'master'},
  0x45A3: {'name': 'TagName', 'type': 'utf-8'},
  0x447A: {'name': 'TagLanguage', 'type': 'string'},
  0x447B: {'name': 'TagLanguageIETF', 'type': 'string'},
  0x4484: {'name': 'TagDefault', 'type': 'uinteger'},
  0x44B4: {'name': 'TagDefaultBogus', 'type': 'uinteger'},
  0x4487: {'name': 'TagString', 'type': 'utf-8'},
  0x4485: {'name': 'TagBinary', 'type': 'binary'}
}