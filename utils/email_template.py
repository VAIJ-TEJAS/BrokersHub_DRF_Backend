def email_template(model_name, instance):
    return """
    <!DOCTYPE HTML
  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title></title>
  <style type="text/css">
    @media only screen and (min-width: 620px) {
      .u-row {
        width: 600px !important;
      }

      .u-row .u-col {
        vertical-align: top;
      }

      .u-row .u-col-100 {
        width: 600px !important;
      }

    }

    @media (max-width: 620px) {
      .u-row-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
      }

      .u-row .u-col {
        min-width: 320px !important;
        max-width: 100% !important;
        display: block !important;
      }

      .u-row {
        width: 100% !important;
      }

      .u-col {
        width: 100% !important;
      }

      .u-col>div {
        margin: 0 auto;
      }
    }

    body {
      margin: 0;
      padding: 0;
    }

    table,
    tr,
    td {
      vertical-align: top;
      border-collapse: collapse;
    }

    p {
      margin: 0;
    }

    .ie-container table,
    .mso-container table {
      table-layout: fixed;
    }

    * {
      line-height: inherit;
    }

    a[x-apple-data-detectors='true'] {
      color: inherit !important;
      text-decoration: none !important;
    }

    @media (max-width: 480px) {
      .hide-mobile {
        max-height: 0px;
        overflow: hidden;
        display: none !important;
      }
    }

    table,
    td {
      color: #000000;
    }

    #u_body a {
      color: #0000ee;
      text-decoration: underline;
    }

    @media (max-width: 480px) {
      #u_content_text_2 .v-container-padding-padding {
        padding: 30px 10px 10px !important;
      }

      #u_content_button_1 .v-size-width {
        width: 65% !important;
      }

      #u_content_button_1 .v-text-align {
        text-align: left !important;
      }

      #u_content_button_1 .v-border-radius {
        border-radius: 4px !important;
        -webkit-border-radius: 4px !important;
        -moz-border-radius: 4px !important;
      }

      #u_content_text_3 .v-container-padding-padding {
        padding: 10px 10px 30px !important;
      }

      #u_content_text_4 .v-container-padding-padding {
        padding: 30px 10px 10px !important;
      }

      #u_content_menu_1 .v-padding {
        padding: 5px 10px !important;
      }

      #u_content_text_5 .v-container-padding-padding {
        padding: 10px 10px 30px !important;
      }
    }
  </style>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Raleway:400,700&display=swap" rel="stylesheet" type="text/css">
</head>

<body>
  <div
    style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="background-color:#004585; height: 40px; padding-top: 20px;">
      <div style="text-align:center;">
        <span style="color: #ffffff; font-size: larger; font-weight: 900;font-family:'Raleway',sans-serif;">
          TheBrokersHub
        </span>
      </div>
    </div>
    <div style="padding: 0px;background-color: transparent">
      <div class="u-row"
        style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
        <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
          <div class="u-col u-col-100"
            style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
            <div
              style="background-color: #f7f7f8;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
              <div
                style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <table id="u_content_text_2" style="font-family:'Raleway',sans-serif;" role="presentation"
                  cellpadding="0" cellspacing="0" width="100%">
                  <tbody>
                    <tr>
                      <td
                        style="overflow-wrap:break-word;word-break:break-word;padding:40px 50px 30px;font-family:'Raleway',sans-serif;">
                        <div style="font-size: 14px; line-height: 140%; text-align: justify; word-wrap: break-word;">
                          <p style="line-height: 140%; font-size: 14px;"><span
                              style="font-family: 'Open Sans', sans-serif; font-size: 16px; line-height: 22.4px;"><strong>Dear
                                Tejas,</strong></span></p>
                          <p style="line-height: 140%; font-size: 14px;"> </p>
                          <p style="line-height: 140%; font-size: 14px;"><span
                              style="font-family: 'Open Sans', sans-serif; font-size: 14px; line-height: 19.6px;">We
                              hope this email finds you well.</span></p>
                          <p style="line-height: 140%; font-size: 14px;"> </p>
                          <p style="line-height: 140%; font-size: 14px;"><span
                              style="font-family: 'Open Sans', sans-serif; font-size: 14px; line-height: 19.6px;">We
                              are reaching out to inform you about a new property requirement in your
                              operational
                              area.</span></p>
                          <p style="line-height: 140%; font-size: 14px;"> </p>
                          <p style="line-height: 140%; font-size: 14px;"><span
                              style="font-family: 'Open Sans', sans-serif; font-size: 14px; line-height: 19.6px;">Here
                              are the details of the client's requirement:
                            </span></p>
                          <p style="line-height: 140%; font-size: 14px;"> </p>
                          <p style="line-height: 140%; font-size: 14px; text-align: center;"><span
                              style="font-family: 'Open Sans', sans-serif; font-size: 18px; line-height: 22.4px; color: #004585;"><strong>Title
                                of the requirement</strong></span></p>
                          <p style="line-height: 140%; font-size: 14px;"> </p>
                          <table
                            style="font-family: 'Open Sans', sans-serif; font-size: 14px; line-height: 140%; width: 100%; border-collapse: collapse;">
                            <tr>
                              <td style="border: 1px solid #000; padding: 8px; width: 60px; text-align: center;">
                                Type</td>
                              <td style="border: 1px solid #000; padding: 8px;">Location</td>
                              <td style="border: 1px solid #000; padding: 8px; width: 90px; text-align: center;">
                                Budget</td>
                            </tr>
                            <tr>
                              <th style="border: 1px solid #000; padding: 8px; text-align: center;">Buy</th>
                              <th style="border: 1px solid #000; padding: 8px;">Pune, Maharashtra</th>
                              <th style="border: 1px solid #000; padding: 8px; text-align: center;">10,00,000
                              </th>
                            </tr>
                          </table>
                          <p style="line-height: 140%; font-size: 14px;"> </p>
                          <p style="line-height: 140%; font-size: 14px;"><span
                              style="font-family: 'Open Sans', sans-serif; font-size: 14px; line-height: 19.6px;">Should
                              you have any properties in your inventory that match these criteria or if you know
                              of any properties that might suit our client's needs, we would greatly appreciate
                              it
                              if you could get in touch with us at your earliest convenience. </span></p>
                          <p style="line-height: 140%; font-size: 14px;"> </p>
                          <p style="line-height: 140%; font-size: 14px;"><span
                              style="font-family: 'Open Sans', sans-serif; font-size: 14px; line-height: 19.6px;">Thank
                              you for your cooperation.
                            </span></p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <table id="u_content_button_1" style="font-family:'Raleway',sans-serif;" role="presentation"
                  cellpadding="0" cellspacing="0" width="100%" border="0">
                  <tbody>
                    <tr>
                      <td class="v-container-padding-padding"
                        style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
                        align="left">
                        <div class="v-text-align" align="center">
                          <a href="https://www.unlayer.com" target="_blank"
                            class="v-button v-size-width v-border-radius"
                            style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #004585; border-radius: 25px;-webkit-border-radius: 25px; -moz-border-radius: 25px; width:30%; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 14px;">
                            <span class="v-padding"
                              style="display:block;padding:10px 20px;line-height:120%;"><strong><span
                                  style="font-size: 14px; line-height: 16.8px;">View
                                  Details</span></strong></span>
                          </a>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <table id="u_content_text_3" style="font-family:'Raleway',sans-serif;" role="presentation"
                  cellpadding="0" cellspacing="0" width="100%" border="0">
                  <tbody>
                    <tr>
                      <td class="v-container-padding-padding"
                        style="overflow-wrap:break-word;word-break:break-word;padding:20px 0px 20px 50px;font-family:'Raleway',sans-serif;"
                        align="left">
                        <div class="v-text-align"
                          style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
                          <p style="font-size: 14px; line-height: 140%;">Subhojit Dey</p>
                          <p style="font-size: 14px; line-height: 140%;">CEO.</p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div style="padding: 0px;background-color: transparent">
      <div class="u-row"
        style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
        <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
          <div class="u-col u-col-100"
            style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
            <div
              style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
              <div
                style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <table id="u_content_text_4" style="font-family:'Raleway',sans-serif;" role="presentation"
                  cellpadding="0" cellspacing="0" width="100%" border="0">
                  <tbody>
                    <tr>
                      <td class="v-container-padding-padding"
                        style="overflow-wrap:break-word;word-break:break-word;padding:40px 80px 10px;font-family:'Raleway',sans-serif;"
                        align="left">
                        <div class="v-text-align"
                          style="font-size: 14px; line-height: 160%; text-align: center; word-wrap: break-word;">
                          <p style="font-size: 14px; line-height: 160%;">if you have any questions, please email
                            us at <a rel="noopener" href="https://www.unlayer.com"
                              target="_blank">support@thebrokershub.in</a></p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0"
                  width="100%" border="0">
                  <tbody>
                    <tr>
                      <td class="v-container-padding-padding"
                        style="overflow-wrap:break-word;word-break:break-word;padding:20px 0px;font-family:'Raleway',sans-serif;"
                        align="left">
                        <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                          style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                          <tbody>
                            <tr style="vertical-align: top">
                              <td
                                style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <span>&#160;</span>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <!-- <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0"
                        cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
                              align="left">
                              <div align="center">
                                <div style="display: table; max-width:187px;">
                                  <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32"
                                    style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 15px">
                                    <tbody>
                                      <tr style="vertical-align: top">
                                        <td align="left" valign="middle"
                                          style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                          <a href="https://www.facebook.com/unlayer" title="Facebook" target="_blank">
                                            <img src="images/image-1.png" alt="Facebook" title="Facebook" width="32"
                                              style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                          </a>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32"
                                    style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 15px">
                                    <tbody>
                                      <tr style="vertical-align: top">
                                        <td align="left" valign="middle"
                                          style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                          <a href="https://twitter.com/unlayerapp" title="Twitter" target="_blank">
                                            <img src="images/image-3.png" alt="Twitter" title="Twitter" width="32"
                                              style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                          </a>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32"
                                    style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 15px">
                                    <tbody>
                                      <tr style="vertical-align: top">
                                        <td align="left" valign="middle"
                                          style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                          <a href="https://www.linkedin.com/company/unlayer/mycompany/" title="LinkedIn"
                                            target="_blank">
                                            <img src="images/image-4.png" alt="LinkedIn" title="LinkedIn" width="32"
                                              style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                          </a>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                  <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32"
                                    style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 0px">
                                    <tbody>
                                      <tr style="vertical-align: top">
                                        <td align="left" valign="middle"
                                          style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                          <a href="https://www.instagram.com/unlayer_official/" title="Instagram"
                                            target="_blank">
                                            <img src="images/image-2.png" alt="Instagram" title="Instagram" width="32"
                                              style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                          </a>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </div>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table> -->
                <!-- <table id="u_content_menu_1" style="font-family:'Raleway',sans-serif;" role="presentation"
                        cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td class="v-container-padding-padding"
                              style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
                              align="left">

                              <div class="menu" style="text-align:center">
                               
                                <a href="https://www.unlayer.com" target="_self"
                                  style="padding:5px 15px;display:inline-block;color:#000000;font-size:14px;text-decoration:none"
                                  class="v-padding">
                                  Home
                                </a>

                                <span style="padding:5px 15px;display:inline-block;color:#000000;font-size:14px;"
                                  class="v-padding hide-mobile">
                                  |
                                </span>

                                <a href="https://www.unlayer.com" target="_self"
                                  style="padding:5px 15px;display:inline-block;color:#000000;font-size:14px;text-decoration:none"
                                  class="v-padding">
                                  Page
                                </a>

                                <span style="padding:5px 15px;display:inline-block;color:#000000;font-size:14px;"
                                  class="v-padding hide-mobile">
                                  |
                                </span>

                                <a href="https://www.unlayer.com" target="_self"
                                  style="padding:5px 15px;display:inline-block;color:#000000;font-size:14px;text-decoration:none"
                                  class="v-padding">
                                  About Us
                                </a>

                                <span style="padding:5px 15px;display:inline-block;color:#000000;font-size:14px;"
                                  class="v-padding hide-mobile">
                                  |
                                </span>

                                <a href="https://www.unlayer.com" target="_self"
                                  style="padding:5px 15px;display:inline-block;color:#000000;font-size:14px;text-decoration:none"
                                  class="v-padding">
                                  Contact US
                                </a>

                              </div>

                            </td>
                          </tr>
                        </tbody>
                      </table> -->
                <table id="u_content_text_5" style="font-family:'Raleway',sans-serif;" role="presentation"
                  cellpadding="0" cellspacing="0" width="100%" border="0">
                  <tbody>
                    <tr>
                      <td class="v-container-padding-padding"
                        style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 40px;font-family:'Raleway',sans-serif;"
                        align="left">
                        <div class="v-text-align"
                          style="font-size: 14px; line-height: 160%; text-align: center; word-wrap: break-word;">
                          <p style="font-size: 14px; line-height: 160%;">you have received this email as a
                            registered user of <a rel="noopener" href="https://www.unlayer.com"
                              target="_blank">thebrokershub.in</a></p>
                          <!-- <p style="font-size: 14px; line-height: 160%;">can <a rel="noopener"
                                    href="https://www.unlayer.com" target="_blank">unsubscribe</a> from these emails
                                  here.</p> -->
                          <p style="font-size: 14px; line-height: 160%;"> </p>
                          <p style="font-size: 14px; line-height: 160%;">2261 Market Street #4667 San Francisco,
                            CA 94114 All rights reserved</p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</body>

</html>
"""
